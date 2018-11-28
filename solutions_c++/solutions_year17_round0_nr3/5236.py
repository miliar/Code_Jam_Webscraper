#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <cstdlib>
#include <time.h>
#include <bits/stdc++.h>
#include <queue>

using namespace std;

struct node{
	int first;
	int second;
};

node a[1000000];
bool operator<(const node & a, const node & b) {
  return ((a.second - a.first) < (b.second - b.first)) || ((a.second - a.first) == (b.second - b.first) and a.first < b.first);
}

int main(){
	int t,k,n,top,rear,l,r,pos;
	cin >> t;
	priority_queue<node> q;
	for(int i = 1;i<=t; i++){
		cin >> n >> k;
		q = priority_queue <node >();
		top = rear = 0;
		node temp,curr;
		temp.first = 2;
		temp.second = n+1;
		q.push(temp);
		//a[rear++] = temp;
		while(k>0){
			//curr = a[top];
			curr = q.top();
			top ++;
			int u = curr.second - curr.first + 1;
			l = curr.first, r = curr.second;
			q.pop();
			//cout << " l r " << l << " " << r << endl;
			if(u % 2 == 0){
				if(k == 1){
					pos = l + u/2 -1;
					break;
				}
				temp.first = l+ u/2 ;
				temp.second = r;
				//if(temp.second >= temp.first)a[rear++] = temp;
				if(temp.second >= temp.first)q.push(temp);
				temp.first = l;
				temp.second = l+u/2 - 2;
				if(temp.second >= temp.first)q.push(temp);
				//if(temp.second >= temp.first)a[rear++] = temp;
				k--;

			}
			else{
				if( k == 1){
					pos = l + u/2;
					break;
				}
				temp.first = l;
				temp.second = l+u/2 -1;
				if(temp.second >= temp.first)q.push(temp);
				//if(temp.second >= temp.first)a[rear++] = temp;
				temp.first = l+ u/2+ 1;
				temp.second = r;
				if(temp.second >= temp.first)q.push(temp);
				//if(temp.second >= temp.first)a[rear++] = temp;
				k--;
			}
		}
		int ls =  pos - l , rs =  r - pos ;
		cout << "Case #" << i << ": " << max(ls,rs) << " " << min(ls,rs) << endl;

	}
}