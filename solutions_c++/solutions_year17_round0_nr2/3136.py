#include <bits/stdc++.h>
#define lld long long

using namespace std;

lld N,ans;

void process(){
	scanf("%lld",&N);
	lld t = N;
	vector<int> tmp;
	while(t != 0){
		tmp.push_back(t%10);
		t /= 10;
	}
    reverse(tmp.begin(),tmp.end());
    lld ten[20];
    ten[0] = 1; for(int i=1; i<20; i++) ten[i] = ten[i-1]*10;
    ans = 0;
    for(int i=0; i<tmp.size(); i++){
        bool flag = true;
        int k = tmp[i];
        for(int j=i+1; j<tmp.size(); j++){
            if(tmp[j] < k){
				flag = false; break;
            }else if(tmp[j] > k) break;
        }
        if(!flag){
            ans += (ten[tmp.size()-1-i]*(k-1));
			for(int j=i+1; j<tmp.size(); j++) ans += (ten[tmp.size()-1-j]*9);
			break;
        }
        ans += (ten[tmp.size()-1-i]*k);
    }
    printf("%lld\n",ans);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for(int i=1; i<=T; i++){
		printf("Case #%d: ",i);
		process();
	}

	return 0;
}
