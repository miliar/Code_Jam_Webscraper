#include <stdio.h>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
	//freopen("input.txt", "r", stdin);
	int n, k;
	int t;
	scanf("%d", &t);
	for(int id=1; id<=t; id++){
		scanf("%d %d", &n, &k);

		int ans;
		int a, b;
		int ta, tb, tcmp;
		int current;
		int start = 1;
		int num[2] = {};
		int oddtemp = 0;
		int eventemp = 0;

		if(k>1){
			if(n%2==0) num[0] = 1;
			else num[1] = 1;

			current = 0;
			while(current + start < k){
				ta = a;
				tb = b;
				if(ta%2==1) tcmp = ta;
				else tcmp = tb;

				a = n/2;
				b = a-1;

				oddtemp = 0;
				eventemp = 0;
				if(((tcmp-1)/2)%2==0){
					eventemp += num[1] * 2;
				}
				else{
					oddtemp += num[1] * 2;
				}
				eventemp += num[0];
				oddtemp += num[0];

				num[0] = eventemp;
				num[1] = oddtemp;

				//printf("%d %d %d Ȧ:%d ¦:%d\n", a, b, start, oddtemp, eventemp);
				current += start;

				if(a%2==0) n=a;
				else n=b;

				start *= 2;

			}
			int step = k-current;
			if(a%2==0){
				if(eventemp >= step){
					ans = a;
				}
				else{
					ans = b;
				}
			}
			else{
				if(oddtemp >= step){
					ans = a;
				}
				else{
					ans = b;
				}
			}
		}
		else{
			ans=n;
		}

		//printf("ans: %d\n", ans);

		int temp = (ans-1)/2;
		int flag = (ans%2==0 ? 1: 0);
		if(ans==0) flag = 0;
		printf("Case #%d: %d %d\n", id, temp+flag, temp);

	}



    return 0;
}
