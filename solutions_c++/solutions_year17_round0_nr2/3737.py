#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<unsigned long long> all;
    vector<string> d[19];
    ifstream in("input2.in");
    ofstream out("output2.out");
    for(int i =0;i<9;i++) {
    	string a;
    	a+= '1'+i;
    	d[1].push_back(a);
    	all.push_back(i);
    }
    for(int i =2;i<=18;i++){
    	for(int j =0;j<d[i-1].size();j++){
    		for(int s = 0;s<9;s++){
    			char c = (char) s+'1';
    			string f = "";
    			f+=c;
    			if(d[i-1][j][0] >= c) {
    				f+= d[i-1][j];
    				d[i].push_back(f);
    				all.push_back(stoull(f,0,0));
    			}
    		}
    	}
    }
    sort(all.begin(),all.end());
    int t;
    in >> t;
    for(int j =0;j<t;j++){
       unsigned long long n ;
       in >> n;
    int ind = upper_bound(all.begin(),all.end(),n) - all.begin();
    out << "Case #" << j+1 << ": " << all[ind-1] <<endl;
    }


    return 0;
}
