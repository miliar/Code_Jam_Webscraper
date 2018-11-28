#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	int numCases;
	ifstream fin("B-small-attempt1.in");
	FILE * fout = fopen("B.out", "w");
	fin >> numCases;
	for (int cases = 1; cases < numCases+1; cases++) {
		long num;
		enum Colour {
			red = 0,
			orange = 1,
			yellow = 2,
			green = 3,
			blue = 4,
			violet = 5
		};
		long counts[6];
		string colors[] = {"R", "O", "Y", "G", "B", "V"};
		fin >> num >> counts[0] >> counts[1] >> counts[2] >> counts[3] >> counts[4] >> counts[5];
		int maxnum = 0;
		int count = 0;
		string ans = "";
		for (int i = 0; i < 6; i++) {
			if (counts[i] > maxnum) {
				maxnum = counts[i];
				ans = colors[i];
				count = i;
			}
		}
		counts[count]--;
		bool beImpossible = false;
		for (int i = 0; i < num-1; i++) {
			if (ans.compare(i, 1, colors[red]) == 0) {
				if (counts[green] > 0) {
					ans += colors[green];
					counts[green]--;
				} else if (counts[yellow] == 0 && counts[blue] == 0) {
					beImpossible = true;
					break;
				} else if (counts[yellow] > counts[blue]) {
					ans += colors[yellow];
					counts[yellow]--;
				} else if (counts[blue] > counts[yellow]) {
					ans += colors[blue];
					counts[blue]--;
				} else if (counts[orange] > counts[violet]) {
					ans += colors[blue];
					counts[blue]--;
				} else if (counts[violet] > counts[orange]) {
					ans += colors[yellow];
					counts[yellow]--;
				} else if (ans[0] == 'B' && i > 0){
					ans += colors[blue];
					counts[blue]--;
				} else {
					ans += colors[yellow];
					counts[yellow]--;
				}
			}
			
			if (ans.compare(i, 1, colors[yellow]) == 0) {
				if (counts[violet] > 0) {
					ans += colors[violet];
					counts[violet]--;
				} else if (counts[red] == 0 && counts[blue] == 0) {
					beImpossible = true;
					break;
				} else if (counts[red] > counts[blue]) {
					ans += colors[red];
					counts[red]--;
				} else if (counts[blue] > counts[red]) {
					ans += colors[blue];
					counts[blue]--;
				} else if (counts[orange] > counts[green]) {
					ans += colors[blue];
					counts[blue]--;
				} else if (counts[green] > counts[orange]){
					ans += colors[red];
					counts[red]--;
				} else if (ans[0] == 'B' && i > 0) {
					ans += colors[blue];
					counts[blue]--;
				} else {
					ans += colors[red];
					counts[red]--;
				}
			}
			
			if (ans.compare(i, 1, colors[blue]) == 0) {
				if (counts[orange] > 0) {
					ans += colors[orange];
					counts[orange]--;
				} else if (counts[red] == 0 && counts[yellow] == 0) {
					beImpossible = true;
					break;
				} else if (counts[red] > counts[yellow]) {
					ans += colors[red];
					counts[red]--;
				} else if (counts[yellow] > counts[red]) {
					ans += colors[yellow];
					counts[yellow]--;
				} else if (counts[violet] > counts[green]) {
					ans += colors[yellow];
					counts[yellow]--;
				} else if (counts[green] > counts[violet]) {
					ans += colors[red];
					counts[red]--;
				} else if (ans[0] == 'Y' && i > 0) {
					ans += colors[yellow];
					counts[yellow]--;
				} else {
					ans += colors[red];
					counts[red]--;
				}
			}
			
			if (ans.compare(i, 1, colors[orange]) == 0) {
				if (counts[blue] > 0) {
					ans += colors[blue];
					counts[blue]--;
				} else {
					beImpossible = true;
					break;
				}
			}
			
			if (ans.compare(i, 1, colors[green]) == 0) {
				if (counts[red] > 0) {
					ans += colors[red];
					counts[red]--;
				} else {
					beImpossible = true;
					break;
				}
			}
			
			if (ans.compare(i, 1, colors[violet]) == 0) {
				if (counts[yellow] > 0) {
					ans += colors[yellow];
					counts[yellow]--;
				} else {
					beImpossible = true;
					break;
				}
			}
		}
		if (!beImpossible) {
			if (ans[0] == 'R') {
				if (ans[num-1] == 'R' || ans[num-1] == 'O' || ans[num-1] == 'V') {
					beImpossible = true;
				}
			} else if (ans[0] == 'B') {
				if (ans[num-1] == 'B' || ans[num-1] == 'G' || ans[num-1] == 'V') {
					beImpossible = true;
				}
			} else if (ans[0] == 'Y') {
				if (ans[num-1] == 'Y' || ans[num-1] == 'G' || ans[num-1] == 'O') {
					beImpossible = true;
				}
			} else if (ans[0] == 'G') {
				if (ans[num-1] != 'R') {
					beImpossible = true;
				}
			} else if (ans[0] == 'O') {
				if (ans[num-1] != 'B') {
					beImpossible = true;
				}
			}  else if (ans[0] == 'V') {
				if (ans[num-1] != 'Y') {
					beImpossible = true;
				}
			}
		}
		if (beImpossible) ans = "IMPOSSIBLE";
		printf("Case #%d: %s\n", cases, ans.c_str());
		fprintf(fout, "Case #%d: %s\n", cases, ans.c_str());
	}
	fin.close();
	fclose(fout);
	return 0;
}
