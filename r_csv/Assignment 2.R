library(rvest)

CSV_wiki <- "https://en.wikipedia.org/wiki/Comma-separated_values"
CSV_html <- read_html(CSV_wiki)

table <- CSV_html %>%
  html_nodes(xpath = '//*[@id="mw-content-text"]/div[1]/table[2]') %>%
  html_table()
table

write.csv(table, "Assignment 2.csv")

