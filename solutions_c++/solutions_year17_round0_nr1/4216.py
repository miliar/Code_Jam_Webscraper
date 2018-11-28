#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	// your code goes here
	char current;
	int t;
	scanf ("%d", &t);
	for (int l = 0; l < t; l++) {
	    int counter = 0, n = 0, k;
	    bool pancakes[1001] = {0};
	    scanf ("%c", &current);
	    scanf ("%c", &current);
	    while (current != ' ') {
	        if (current == '+') {
	            pancakes[n] = 1;
	        }
	        n++;
	        scanf ("%c", &current);
	    }
	    scanf ("%d", &k);
	    /*cout << n << endl;
	    for (int x = 0; x < n; x++) {
	        cout << pancakes[x] << " ";
	    } cout << endl;*/
	    for (int x = 0; x <= (n - 1 - (k - 1)); x++) {
	        if (!pancakes[x]) {
	            for (int i = x; i < x + k; i++) {
	                pancakes[i] = !pancakes[i];
	            }
	            counter++;
	        }
	    }
	    /*for (int x = 0; x < n; x++) {
	        cout << pancakes[x] << " ";
	    } cout << endl;*/
	    for (int x = 1; x < n; x++) {
	        if (!pancakes[x]) {
	            printf ("Case #%d: Impossible\n", (l+1));
	            break;
	        } else if (x == n - 1) {
	            printf ("Case #%d: %d\n", (l+1), counter);
	        }
	    }
	}
	return 0;
}