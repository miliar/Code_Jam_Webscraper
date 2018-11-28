#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define test(t) int t; scanf("%d", &t); while(t--)
#define forr(I, a, b) for(int I = a; I < b; I++)
#define pb push_back

int main(){
	int T;
	scanf("%d", &T);
	forr(t, 0, T){
		string S;
		cin >> S;
		int maxx = 0;
		while(1){
			maxx = 0;
			bool flag = true;
			forr(i, 0, S.size()){
				int k = S[i] - '0';
				//printf("k : %d \n", k);
				if(k > maxx)
					maxx = k;
				else if(k < maxx){
					flag = false;
					S[i - 1] = maxx - 1 + '0';
					forr(j, i, S.size())
						S[j] = '9';
				}				
				//printf("maxx : %d\n", maxx);
				//cout << S ;
			}
			if(flag)
				break;
		}
		forr(i, 0, S.size()){
			while(S[i] == '0'){
				S.erase(S.begin() + 0);
				i--;
			}
		}
		printf("Case #%d: ", t + 1);
		cout << S << endl;
	}
    return 0;
}