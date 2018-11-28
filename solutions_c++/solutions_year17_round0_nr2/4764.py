#include<bits/stdc++.h>
using namespace::std;
deque<int> d;
long long x;
int t, nc=1;

bool correct(){
	for(int i = 1; i < d.size(); ++i)
		if(d[i] < d[i-1]) return false;
	return true;
}

void update(){
	for(int i = 1; i < d.size(); ++i)
		if(d[i] < d[i-1]){
			d[i-1]--;
			for(int j = i; j < d.size(); ++j)				
				d[j] = 9;
			break;
		}	
}


int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%lld", &x);
		
		d.clear();
		while(x){
			d.push_front(x%10);
			x/=10;
		}

		while(not correct())
			update();
	
		printf("Case #%d: ", nc++);
		bool ok = true;
		for(int i = 0; i < d.size(); ++i)
			if(not ok) putchar('0' + d[i]);
			else if(d[i]) putchar('0' + d[i]), ok = false;
		puts("");
		
	}
	return 0;
}
