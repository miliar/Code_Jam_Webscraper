#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

#define LL long long
#define INF (1LL<<60)

int T, nCase;
int N;
char color[] = {" RYOBVG"};
int c[7];

void swap(int& a, int& b)
{
	int t = a;
	a = b; b = t;
}

string merge(string& s1, string& s2)
{
	string m = "";
	int i, j;
	while (i < s1.length() && j < s2.length()) {
		m += s1[i++];
		m += s2[j++];
	}
	while (i < s1.length()) {
		m += s1[i++];
	}
	return m;
}

string solv()
{
	int order[3] = {1, 2, 4};

	if (c[order[0]] < c[order[1]]) swap(order[0], order[1]); 
	if (c[order[0]] < c[order[2]]) swap(order[0], order[2]); 
	if (c[order[1]] < c[order[2]]) swap(order[1], order[2]); 
	
	if (c[order[0]] > N / 2) return "IMPOSSIBLE";
	
	
	string S1 = string(c[order[0]], color[order[0]]);
	string S2 = string(c[order[1]], color[order[1]]);
	string S3 = string(c[order[2]], color[order[2]]);

	
	S2 += S3;
	S2.resize(S1.length());
	S3.resize(N-S1.length() * 2);

	S1 = merge(S1, S2);
	return merge(S1, S3);
}

int main ()
{
	cin >> T;
	for (nCase = 1; nCase <= T; ++nCase) {
		cin >> N;
		// R, O, Y, G, B, V
		cin >> c[1] >> c[3] >> c[2] >> c[6] >> c[4] >> c[5];
		cout << "Case #" << nCase << ": " << solv() << endl;
	}
	return 0;
}