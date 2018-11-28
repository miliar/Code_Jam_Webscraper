#include <bits/stdc++.h>
using namespace std;

#define MAXN 1005

bool visit[MAXN];
int size;

void solve(int k){
	int max, counter, start, middle, ls, rs;
	while(k > 0){
		max = 0, start = 0;
		for (int i = 0; i < size; ++i)
		{
			counter = 0;
			while(!visit[i]){
				i++;
				counter++;
			}
			if(counter > max){
				max = counter;
				start = i - counter;
			}
		}
		middle = (int)(start + max/2);
		visit[middle] = true;
		ls = middle - start;
		rs = max - ls - 1;
		k--;
	}

	if(rs>ls){
		rs = rs + ls;
		ls = rs - ls;
		rs = rs - ls;
	}
	cout<<ls<<" "<<rs<<endl;
}

int main(){
	int T, n, k;
	cin>>T;
	for (int j = 1; j <= T; ++j)
	{
		memset(visit, false, sizeof visit);
		cin>>n;
		size = n+2;
		visit[0] = visit[size-1] = true;
		cin>>k;
		cout<<"Case #"<<j<<": ";
		solve(k);
	}

	return 0;
}