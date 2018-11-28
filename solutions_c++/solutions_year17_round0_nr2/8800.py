#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
        long long n;
        cin>>n;
        bool flag=0;
        while(n>=10 && !flag){
            long long i=n;
            int temp=9;
            int last;
            while(i>0){
                last=i%10;
                if(last>temp)
                break;
                i=i/10;
                temp=last;
            }
            if(i==0)
            flag=1;
            else
            n--;
        }
        printf("Case #%d: %lld\n",t,n);
	}
	return 0;
}
