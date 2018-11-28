#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
ll  n;
vector<int> digits,newd;

int main(){
	int t,t1 = 1;
	scanf("%d",&t);
	int i,j;
	while(t--){
		digits.clear();
		newd.clear();
		scanf("%lld",&n);
		ll dup = n;
		while(dup > 0){
			digits.push_back(dup%10);
			dup = dup/10;
		}
		ll num = 0;
		reverse(digits.begin(),digits.end());
		newd = digits;
		//for(i = 0 ; i < digits.size() ; i++){printf("%d ",newd[i]);}printf("\n");
		if(digits.size() == 1){
			printf("Case #%d: %lld\n",t1,n);
		}
		else{
			
			while(1){
				//find di > di+1
				int flag = -1,pos = -1;
				for(i = 0 ; i <= newd.size()-2 ; i++){
					if(newd[i] > newd[i+1]){
						flag = 0;
						pos = i;
						break;
					}
				}
				if(flag == -1){
					break;
				}
				//printf("%d\n",pos);
				newd[pos] -= 1;
				for(i = pos + 1 ; i < newd.size() ; i++){
					newd[i] = 9;
				} 
			}
			num = 0;
			for(i = 0 ; i < newd.size() ; i++){
				num = 10*num + newd[i];
			}
			printf("Case #%d: %lld\n",t1,num);
		}
		t1++;
	}
}