#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <cstdio>
using namespace std;

void flip(char& ch){
    if(ch=='+') ch = '-';
    else ch = '+' ;
}

bool isSame(const string& s, int start){
    for(int i = start+1; i<s.size(); ++i){
        if(s[i]!= s[start]) return false;
    }
    return true;
}

int fun(string& s, int k){
    int i = 0, counter = 0;
    while(i<s.size()-k){
        if(s[i]=='+') ++i;
        else{
            int j = 0;
            while(s[i]=='-' and j < k){
                ++i;
                ++j;
            }
            for(int jj = 0; jj < k - j; ++ jj) flip(s[i+jj]);
            ++counter;
        }
    }
    if(isSame(s,i)){
        if(s[i]=='-'){
            if(i==s.size()-k) ++counter;
            else counter = -1;
        }
    }
    else{
        counter = -1;
    }
    return counter;

}

int main()
{
    freopen("D://A-large.in", "r", stdin);
    freopen("D://A-large.out", "w", stdout);

	int numCase;
	cin >> numCase;
//	cout<<setiosflags(ios::fixed);
//	cout<<setprecision(7);
	for(int i=0; i<numCase; i++) {
        string s;
        int k;
		cin>>s>>k;
		int counter = fun(s,k);
		if(counter == -1) cout << "Case #" << (i+1) << ": IMPOSSIBLE" << endl;
        else cout << "Case #" << (i+1) << ": " << counter << endl;
	}
	return 0;
}
