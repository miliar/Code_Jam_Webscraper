#include <iostream>
#include <cstdio>
#include <stdio.h>
#include <string>
#include <cstring>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <ctime>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <utility>
using namespace std;

int main()
{
	int n;
	cin>>n;
	string s;
	long long count =0;
	int k;
	for(int i=1;i<=n;i++){
		count = 0;
		cin>>s;
		cin>>k;
		int l = s.size();
		bool check[l];
		for(int j=0;j<l;j++){
			if(s[j]=='-')
				check[j] = false;
			else
				check[j] = true;
			//cout<<check[j]<<endl;
		}
		for(int j=0;j<=l-k;j++){
			if(check[j]==true){
				continue;
			}else{
				count++;
				//cout<<j<<endl;
				for(int p=j;p<j+k;p++){
					if(p>=l){
						break;
					}else{
						if(check[p]==false){
							check[p]=true;
						}else{
							check[p]=false;
						}
					}
				}
			}
		}
		bool flag=true;
		for(int j=0;j<l;j++){
			if(check[j]==false){
				flag = false;
				break;
			}
		}
		if(flag==true){
			cout<<"Case #"<<i<<": "<<count<<endl;
		}else{
			cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}