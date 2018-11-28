// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <queue>

using namespace std;

void solve()
{
	int k;
	int flips = 0;
	queue<bool> q;
	string pancakes;
	cin >> pancakes;
	cin >> k;
	for (int i = 0; i < pancakes.length() && i < k; i++) {
		if (pancakes[i] == '+')
			q.push(true);
		else {
			q.push(false);
		}
	}
	for (int i = k; i < pancakes.length(); i++) {
		if (q.front() == false) {
			queue<bool> newq;
			while (!q.empty()) {
				newq.push(q.front() ^ true);
				q.pop();
			}
			q = newq;
			flips++;
		}
		q.pop();
		if (pancakes[i] == '+')
			q.push(true);
		else {
			q.push(false);
		}
	}
	if (q.front() == false) {
		queue<bool> newq;
		while (!q.empty()) {
			newq.push(q.front() ^ true);
			q.pop();
		}
		q = newq;
		flips++;
	}

	bool good = true;
	while (!q.empty()) {
		if (q.front() == false) {
			good = false;
			break;
		}
		q.pop();
	}

	if (good) {
		cout << flips;
	}
	else {
		cout << "IMPOSSIBLE";
	}
}

int  main() {
	int k;
	cin >> k;
	for (int i = 0; i < k; i++) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}

	return 0;
}

