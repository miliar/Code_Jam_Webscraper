#include <bits/stdc++.h>
using namespace std;
#define ll long long int



int main(){
#ifndef LOCAL
    ifstream cin("input.in");
    ofstream cout("output.out");
#endif
   int g;
   cin>>g;
   for(int t =  1 ;t<=g;t++){
        vector< pair <int , int > >  v;
        int n;
        cin>>n;
        for(int i = 0;i<6;i++){
        	int x;
        	cin>>x;
        	v.push_back(make_pair(x,i));
        }
        char cor[] = {'R' , 'O' , 'Y' ,'G' ,'B' , 'V'};
        sort(v.rbegin() , v.rend());
        bool flag = true;
        if(v[0].first > v[1].first + v[2].first) flag = false;
       cout<<"Case #"<<t<<":"<<" ";
       if(!flag) cout<<"IMPOSSIBLE"<<endl;
       else{
       	for(int i = 0;i<v[0].first - v[1].first;i++){
       		cout<<cor[v[0].second]<<cor[v[2].second];
       		v[2].first--;
       	}
       	v[0].first  = v[1].first;
       	for(int i = 0;i<v[2].first;i++){
       		cout<<cor[v[0].second]<<cor[v[1].second]<<cor[v[2].second];
       		v[0].first -- , v[1].first --;
       	}
       	for(int i = 0;i<v[0].first;i++){
       		cout<<cor[v[0].second]<<cor[v[1].second];
       	}
       	cout<<endl;
       }
   
}
}