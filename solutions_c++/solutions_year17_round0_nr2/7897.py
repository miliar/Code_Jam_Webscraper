#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

const int M = 18;
int r[M+1];
int s[M+1];
int q[M+1];

int main() {
	ios_base::sync_with_stdio(false);
	int T;
	scanf("%d\n", &T);
	for(int t = 1; t <= T; t++) {
		long long int N;
		scanf("%lld", &N);
		int digits = 0;
		long long int n = N;
		
		for(int i = 0; n; i++) {
			r[i] = n%10;
			n = n/10;
			digits++;
		}

		for(int i = 0; i < digits; i++) {
			s[i] = r[digits - i - 1];
		}

		bool isPivot = false;
		bool isSpecialPivot = false;
		int breakPoint = 0;

		for(int i = 0; i < digits - 1; i++) {
			isPivot = s[i] > s[i+1];
			isSpecialPivot = (s[i] == 1) && isPivot;

			if(isPivot || isSpecialPivot) {
				breakPoint = i;
				break;
			}

		}
		
		if(isPivot && isSpecialPivot) {
			cout<<"Case #"<<t<<": ";
			
			for(int i = 0; i < digits - 1; i++) 
				printf("9");
			printf("\n");
		} else if(isPivot && !isSpecialPivot) {
			for(int i = breakPoint; i > 0; i--) {
				if(s[i-1] == s[i]) {
					breakPoint = i-1;
				}
				else 
					break;
			}

			for (int i = 0; i < digits; i++) {
				if(i < breakPoint)
					q[i] = s[i];
				else if(i == breakPoint)
					q[i] = s[i] - 1;
				else
					q[i] = 9;
			}			
			cout<<"Case #"<<t<<": ";
			for(int i = 0; i < digits; i++)
				printf("%d", q[i]);
			printf("\n");
		} else if(!isPivot) {
			cout<<"Case #"<<t<<": "<<N<<endl;
		}


		/*if(!ok) 
			cout<<"Case #"<<t<<": "<<ans<<endl;
		else
			cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
			*/
	}
	return 0;
}
