#include<bits/stdc++.h>
using namespace std;

int grp[105];

int main()
{
	int N,it,i,T,P;

	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for(it=1; it<=T; it++){

		scanf("%d%d", &N, &P);
		for(i=0; i<N; i++){
			scanf("%d", &grp[i]);
			grp[i] = grp[i]%P;
		}

		int ans = 0;

		if(P==2){
			int odd = 0;
			for(i=0; i<N; i++){
				if(grp[i])  odd++;
				else ans++;
			}
			ans += (odd+1)/2;
		}

		else if(P==3){

			int mod1 = 0, mod2 = 0;

			for(i=0; i<N; i++){
				if(grp[i] == 1)  mod1++;
				else if(grp[i] == 2)  mod2++;
				else ans++;
			}

			if(mod1 > mod2){

				ans += mod2;
				mod1 -= mod2;
				ans += (mod1+2)/3;

			}

			else{

				ans += mod1;
				mod2 -= mod1;
				ans += (mod2+2)/3;
			}
		}

		else if(P==4){

			
			int mod1 = 0, mod2 = 0, mod3 = 0;
			for(i=0; i<N; i++){
				if(grp[i] == 1)  mod1++;
				else if(grp[i] == 2)  mod2++;
				else if(grp[i] == 3)  mod3++;
				else ans++;
			}

			//printf("%d %d %d %d\n", ans, mod1, mod2, mod3);

			ans += (mod2/2);
			mod2 = mod2%2;
			int mn = min(mod1, mod3);
			//printf("mn:%d\n", mn);
			ans += mn;
			mod1 -= mn;
			mod3 -= mn;

			if(mod2 > 0){
				if(mod1 >= 2){
					ans++;
					mod1 -= 2;
					mod2--;
				}
				else if(mod3>=2){
					ans++;
					mod3 -= 2;
					mod2--;
				}

			}

			if(mod1>0)
				ans += (mod1+3)/4;
			if(mod3>0)
				ans += (mod3+3)/4;
			if(mod2>0 && (mod1%4==0 && mod3%4==0))
				ans++;
		}

		printf("Case #%d: %d\n", it, ans);
	}
	return 0;
}