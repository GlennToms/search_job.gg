import requests
from bs4 import BeautifulSoup


def main(lst):
    url = "https://www.gov.gg/jobcentrevacancies?sort=Relevance&size=100#top"
    data = requests.get(url)
    results = BeautifulSoup(data.text, "html.parser").find(id="results")

    for item in results.find_all("li"):
        a, title, company, time, ref, b, start, end, c, d = item.text.split("\n")
        check = ref[5:] + "\n"
        ref = ref[5:]
        if check not in lst:
            print(f"title: {title}")
            print(f"company: {company}")
            print(f"time: {time}")
            print(f"ref: {ref}")
            print(f"start: {start}")
            print(f"end: {end}")
            print(f"a: {a}")
            print(f"b: {b}")
            print(f"c: {c}")
            print(f"d: {d}")
            if input("skip y/n \n").lower() == "y":
                writetofile(ref, "ref.txt")
            else:
                writetofile(ref, "keep.txt")


def writetofile(ref, file):
    with open(file, "a") as file:
        file.writelines(f"{ref}\n")


def read(f):
    with open(f, "r") as file:
        return file.readlines()


lst = list(read("ref.txt"))
lst.append(list(read("keep.txt")))
main(lst)
