#include<map> 
#include<set>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

typedef unsigned long long ull;

int main(){

	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	map<ull,ull> num;

	ull n,k;

	int ntc;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> n >> k;
		num.clear();
		num[n]+=1;
		while(1){
			ull n = num.rbegin()->first;
			ull t = num.rbegin()->second;
			if (k>t){
				k-=t;
				if (n&1)
					num[n/2]+=2*t;
				else
					num[n/2]+=t,num[n/2-1]+=t;
				num.erase(--num.end());
			}
			else{
				cout << "Case #" << tc << ": ";
				if (n&1)
					cout << n/2 << " " << n/2 << endl;
				else
					cout << n/2 << " " << n/2-1 << endl;
				break;
			}
				
		}

	}

	return 0;
}