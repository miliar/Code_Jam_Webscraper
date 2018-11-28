#include <bits/stdc++.h>

using namespace std;

void _main (int TEST) {
    // Code goes here
    int N, D;
    cin >> D >> N;
    vector<int> t(N);
    double largest = 0; // out of highest
    for (int i = 0; i < N; i++) {
        int p, s;
        cin >> p >> s;
        double t = ((double)(D-p))/((double)s);
        if (t > largest)
            largest = t;
    }
    printf("%0.6f\n",((double)D)/largest);
    cerr << "Solved test case #" << TEST << endl;
}

int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for (int i = 1; i <= TEST; i++) {
	printf("Case #%d: ", i);
	_main(i);
    }
    return 0;
}
