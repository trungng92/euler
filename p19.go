// You are given the following information, but you may prefer to do some research for yourself.

// 1 Jan 1900 was a Monday.
// Thirty days has September,
// April, June and November.
// All the rest have thirty-one,
// Saving February alone,
// Which has twenty-eight, rain or shine.
// And on leap years, twenty-nine.
// A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
// How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
//
// NOTE: This is asking you how many months from January 1901 to December 2000 started with a Sunday
// NOT how many sundays were in the first month of the year from January 1901 to December 2000

package main

import "time"

func main() {
	totalSundays := 0
	for year := 1901; year < 2001; year++ {
		for month := time.January; month <= time.December; month++ {
			t := time.Date(year, month, 1, 0, 0, 0, 0, time.UTC)
			if t.Weekday() == 0 {
				totalSundays++
			}
		}
	}
	println("total sundays from 1, 1901 to 12, 2000:", totalSundays)
}
