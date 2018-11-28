#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define pll pair<ll, ll>
#define F first
#define S second
#define mp make_pair
#define pb push_back

int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		int N, R, Y, B, O, V, G;
		cin >> N >> R >> O >> Y >> G >> B >> V;
		string ans = "";
		for(int i = 0; i < N; i++)
		{
			ans = ans + "O";
		}
		int small, mid, large;
		char one, two, three;
		if(R <= B && R <= Y){
			small = R;
			one = 'R';
			if(B <= Y){
				mid = B;
				two = 'B';
				large = Y;
				three = 'Y';
			}
			else
			{
				mid = Y;
				two = 'Y';
				large = B;
				three = 'B';	
			}
		}
		else if(B <= R && B <= Y){
			small = B;
			one = 'B';
			if(R <= Y){
				mid = R;
				two = 'R';
				large = Y;
				three = 'Y';
			}
			else
			{
				mid = Y;
				two = 'Y';
				large = R;
				three = 'R';	
			}
		}
		else if(Y <= B && Y <= R){
			small = Y;
			one = 'Y';
			if(B <= R){
				mid = B;
				two = 'B';
				large = R;
				three = 'R';
			}
			else
			{
				mid = R;
				two = 'R';
				large = B;
				three = 'B';	
			}
		}
		if(large <= small + mid){
			for(int i = 0, j = 0; j < large; i += 2, j++) {
				ans[i] = three;
			}
			for(int i = 2*large - 1; i < N; i++)
			{
				if(i % 2){
					ans[i] = two;
					mid -= 1;
				}
				else{
					ans[i] = one;
					small -= 1;
				}
			}
			for(int i = 1, j = 0; j < mid; i+= 2, j++) {
				ans[i] = two;
			}
			for(int i = 2*mid + 1, j = 0; j < small; i += 2, j++) {
				ans[i] = one;
			}
		}
		else
		{
			ans = "IMPOSSIBLE";
		}
		// printf("Case #%d: %s\n", t, ans);
		cout << "Case #" << t << ": " << ans << endl;

	}
	return 0;
}