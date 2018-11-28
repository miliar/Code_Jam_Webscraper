#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
char str[1010];
char conv[3];
void solve(int casen)
{
	int pos = 0;
	int N, R, O, Y, G, B, V;
	cin >> N >> R >> O >> Y >> G >> B >> V;
	vector<int> a(3); a[0] = R; a[1] = Y; a[2] = B;
	sort(a.begin(), a.end());
	reverse(a.begin(), a.end());
	if (R == a[0]) {
		conv[0] = 'R';
		if (Y == a[1]) {
			conv[1] = 'Y';
			conv[2] = 'B';
		}
		else {
			conv[1] = 'B';
			conv[2] = 'Y';
		}
	}
	else if(Y == a[0]) {
		conv[0] = 'Y';
		if (B == a[1]) {
			conv[1] = 'B';
			conv[2] = 'R';
		}
		else {
			conv[1] = 'R';
			conv[2] = 'B';
		}
	}
	else if (B == a[0]) {
		conv[0] = 'B';
		if (Y == a[1]) {
			conv[1] = 'Y';
			conv[2] = 'R';
		}
		else {
			conv[1] = 'R';
			conv[2] = 'Y';
		}
	}
	if (a[0] > a[1] + a[2]) {
		printf("Case #%d: IMPOSSIBLE\n", casen);
		return;
	}
	for (int i = 0; i < a[0]; i++)
	{
		str[pos++] = 0;
		if (i < a[1]) str[pos++] = 1;
		if (a[0] - a[2] <= i) str[pos++] = 2;
	}
	for (int i = 0; i < pos; i++) str[i] = conv[str[i]];
	str[pos] = '\0';
	printf("Case #%d: %s\n", casen, str);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; cin >> t;
	for (int i = 1; i <= t; i++) solve(i);
}