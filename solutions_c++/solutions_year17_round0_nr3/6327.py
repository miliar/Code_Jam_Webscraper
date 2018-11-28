#include <iostream>
#include <fstream>
#include <algorithm>    
#include <vector> 
using namespace std;
#define ll long long
ll length;
ll number;
ll large, small;
void compute(){
	ll input[] = {length};
	vector<ll> v(input, input + 1);
	make_heap(v.begin(), v.end());
	ll temp;
	while ( number > 1 ){
		pop_heap(v.begin(), v.end());
		temp = v.back();
		v.pop_back();
		v.push_back((temp - 1) / 2);
		push_heap (v.begin(),v.end());
		v.push_back(temp - 1 - (temp - 1) / 2);
		push_heap (v.begin(),v.end());
		number --;
	}
	pop_heap(v.begin(), v.end());
	temp = v.back();
	small = (temp - 1) / 2;
	large = temp - 1 - (temp - 1) / 2;
}
int main(){ 
    ofstream fout("A.out"); 
	int n;
	cin >> n;
	for ( int i = 0 ; i < n ; i ++ ){
		cin >> length >> number;
		compute();
		fout << "Case #" << i + 1 <<": " << large << " " << small <<  endl;
		continue;
	}
	
	return 0;
}
