// Syed Ghulam Akbar
// CodeJam 2016

#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

void main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int testCount;
	scanf("%d",&testCount);

	for (int test=1;test<=testCount;test++) {
		char cakes[2000];
		int K=0;
		int flips = 0;

		// Read the problem input
		cin >> cakes;
		cin >> K;

		// Now check each cake from the left, and see if it's happy face or not
		// If it's not happy face, try to flip all cakes from current cake to right
		int count = strlen(cakes);
		for (int i=0; i< count; i++) {

			// If already a happy face, no need to worry about flipping it
			if (cakes[i] == '+')
				continue;

			// Now flip and the next K cakes
			if (i + K <= count) {

				// Flip next K cakes
				for (int j=i; j<i+K; j++) {
					cakes[j] = (cakes[j] == '+') ? '-' : '+';
				}

				// Increment flip counter
				flips++;
			} else {
				// Reached boundry limit, as we can't flip all cakes to happy face, abort
				// the current loop as well
				flips = -1;
				break;
			}
		}

		cout << "Case #" << test << ": ";
		if (flips < 0)
			cout << "IMPOSSIBLE";
		else
			cout << flips;

		cout << "\n";
	}
}
