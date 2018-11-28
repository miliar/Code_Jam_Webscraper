#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <cstdio>
using namespace std;

unsigned long long int tidy(unsigned long long int x){
    vector<unsigned int> v;
    unsigned long long int res=0;
    bool flag = false;
    while(x){
        int tmp = x % 10;
        v.push_back(tmp);
        x /= 10;
    }
    for(int i = v.size()-2; i >= 0; --i){
        if(flag) v[i] = 9;
        else{
            if(v[i] < v[i+1]){
                flag = true;
                int j = i+1;
                while(j< v.size()){
                    if(v[j] > v[j-1]){
                        v[j-1]  = 9;
                        v[j++] -=1;
                    }
                    else break;
                }
            }
        }
    }
    for(int i=v.size()-1; i>=0; --i){
        res *= 10;
        res += v[i];
    }
    return res;
}


int main()
{

    freopen("d://B-large.in", "r", stdin);
    freopen("d://B-large.out", "w", stdout);

	int numcase;
	cin >> numcase;
//	cout<<setiosflags(ios::fixed);
//	cout<<setprecision(7);
	for(int i=0; i<numcase; i++) {
        unsigned long long int x;
		cin>>x;
        cout << "case #" << (i+1) << ": " << tidy(x) << endl;
	}
	return 0;
}
