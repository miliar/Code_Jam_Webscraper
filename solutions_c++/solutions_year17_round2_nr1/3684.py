#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <cmath>
#include <climits>
#include <queue>
#include <iomanip>
#include <cstdio>
#define lli long long int
#include<fstream>
using namespace std;

int main()
{
    ifstream cin("A-large.in");
	ofstream cout("output.txt");
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++){
            cout<<"Case #"<<tt<<": ";
        int d,n,k,s;
		cin>>d>>n;
		double hrs=INT_MIN;
		for (int i=0;i<n;i++){
			cin>>k>>s;
			hrs=max(hrs,(d-k)/(s*1.0));
		}
		std::cout << std::fixed;
		cout << std::setprecision(9) << d/hrs << endl;



    }
}


