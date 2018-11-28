/*************************************************************************
    > File Name: qua2.cpp
    > Author: Yuchen Wang
    > Mail: wyc8094@gmail.com 
    > Created Time: Sat Apr  8 14:42:20 2017
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

typedef long long ll;

ll n;
int t,digitn;
int spdigit[20];

void split()
{
	memset(spdigit,0,sizeof(spdigit));
	digitn = 0;
	ll tmpn = n;
	for(int i=0;tmpn;i++){
		spdigit[i] = tmpn%10;
		tmpn /= 10;
		digitn++;
	}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	int tt = 0;
	cin >> t;
	while(t--){
		printf("Case #%d: ",++tt);
		int flag = 0;
		cin >> n;
		split();

		for(int i=digitn-2;i>=0;i--){
			if(spdigit[i]<spdigit[i+1]){
				for(int j=i+1;j<digitn;j++){
					spdigit[j]--;
					if(spdigit[j]<0){
						spdigit[j] = 9;
						spdigit[j+1]--;
						continue;
					}
					else if(spdigit[j]>=spdigit[j+1])break;
					else{
						spdigit[j] = 9;
					}
				}
				for(int j=i;j>=0;j--)spdigit[j]=9;
				break;
			}
		}

		for(int j=digitn-1;j>=0;j--){
			if(!flag && spdigit[j]==0)continue;
			else{
				flag = 1;
				cout << spdigit[j];
			}
		}

		cout << endl;
	}
	return 0;
}

