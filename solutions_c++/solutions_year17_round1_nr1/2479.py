#include<bits/stdc++.h>
using namespace std;
#define N 60
string arr[N];
bool mark[N];
int main(){
	int t,r,c;
    cin>>t;
    for (int i = 1; i <= t; ++i){
      cin>>r>>c;
      for (int j = 0; j < r; ++j){
      	cin>>arr[j];
      }
      int last = 0;
      for (int f = 0; f < r; ++f){
      	for (int h = 0; h < c; ++h){
      		if(arr[f][h] != '?' ){
      			char L = arr[f][h];
      			int m = h+1;
      			while(m < c && arr[f][m] == '?'){
      				arr[f][m] = L;
      				m++;
      			}
      		}
      	}
      	for (int h = c-1; h >= 0; h--){
      		if(arr[f][h] != '?' ){
      			char L = arr[f][h];
      			int m = h-1;
      			while(-1 < m && arr[f][m] == '?'){
      				arr[f][m] = L;
      				m--;
      			}
      		}
      	}
      }

      for (int h = 0; h < c; ++h){
      	for (int f = 0; f < r; ++f){
      		if(arr[f][h] != '?' ){
      			char L = arr[f][h];
      			int m = f+1;
      			while(m < r && arr[m][h] == '?'){
      				arr[m][h] = L;
      				m++;
      			}
      		}
      	}
      	for (int f = r-1; f >= 0; f--){
      		if(arr[f][h] != '?' ){
      			char L = arr[f][h];
      			int m = f-1;
      			while(-1 < m && arr[m][h] == '?'){
      				arr[m][h] = L;
      				m--;
      			}
      		}
      	}
      }
      cout<<"Case #"<<i<<":"<<endl;
      for (int j = 0; j < r; ++j)
      {
      	cout<<arr[j]<<endl;
      }

    }
}