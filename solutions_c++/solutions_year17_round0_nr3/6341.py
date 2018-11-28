#include <cstdio>

using namespace std;

int main()
{
	int num,round=0;
	scanf("%d",&num);
	for(int i=0;i<num;++i){
		round++;
		long long int room, man, rman;
		scanf("%lld %lld",&room,&man);
		long long int dir[64], fi[64];
		rman = man;
		int cnt=0;
		if(man==1){
			if(room%2)
				printf("Case #%d: %lld %lld\n",round,room/2,room/2);
			else
				printf("Case #%d: %lld %lld\n",round,room/2,room/2-1);
			continue;
		}
		for(int j=0;j<64;++j){
			dir[j]=2;
			fi[j]=-1;
		}
		while(man){
			fi[cnt]=man;
			man /= 2;
			cnt++;
		}
		man=1;
		int cnt2=1;
		for(int j=cnt-2;j>=0;--j){
			if(man*2 == fi[j]){
				dir[cnt2]=0;
				man*=2;
			}
			else{
				dir[cnt2]=1;
				man = man*2 + 1;
			}
			cnt2++;
		}
		long long int posi[2], tmp, A, B, la, lb, ta=0, tb=0;
		if(room%2){
			posi[0]=room/2;
			posi[1]=room/2;
			A=2;B=0;
		}
		else{
			posi[0]=room/2;
			posi[1]=room/2-1;
			A=1;B=1;
		}
		long long int big[2], sma[2];
		big[0] = posi[0];
		sma[1] = posi[1];
		for(int j=1;j<cnt2;++j){
			if(sma[1] != big[0]){
				if(big[0]%2){
					big[0]=big[0]/2;
					big[1]=big[0];
					ta += 2*A;
				}
				else{
					big[0]=big[0]/2;
					big[1]=big[0]-1;
					ta += A;
					tb += A;
				}
				if(sma[1]%2){
					sma[0]=sma[1]/2;
					sma[1]=sma[0];
					tb += 2*B;
				}
				else{
					sma[0]=sma[1]/2;
					sma[1]=sma[0]-1;
					ta += B;
					tb += B;
				}
			}else if(sma[1] == big[0]){
				if(big[0]%2){
					big[0]=big[0]/2;
					big[1]=big[0];
					ta += 2*A;
				}
				else{
					big[0]=big[0]/2;
					big[1]=big[0]-1;
					ta += A;
					tb += A;
				}
				if(sma[1]%2){
					sma[0]=sma[1]/2;
					sma[1]=sma[0];
				}
				else{
					sma[0]=sma[1]/2;
					sma[1]=sma[0]-1;
				}
			}
			la = A;
			lb = B;
			A = ta;
			B = tb;
			ta = 0;
			tb = 0;
			if(j == cnt2-1){
				long long int two=1;
				for(int k=1;k<cnt;++k)
					two*=2;
				two--;
				rman = rman - two;
				if(rman <= la){
					posi[0]=big[0];
					posi[1]=big[1];
					if(posi[1]<0)
						posi[1]=0;
				}
				else{
					posi[0]=sma[0];
					posi[1]=sma[1];
					if(posi[1]<0)
						posi[1]=0;
				}
				break;
			}
		}
		printf("Case #%d: %lld %lld\n",round,posi[0],posi[1]);
	}
	return 0;
}
