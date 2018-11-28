#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>
using namespace std;

typedef long long int ll;

vector<int> NOL(ll num) {
    vector<int> myList;
    while(num > 0) {
        int d = num%10;
        num /=10;
        myList.push_back(d);
    }
    reverse(myList.begin(), myList.end());
    return myList;
}

string NumberToString ( ll Number )
  {
     stringstream ss;
     ss << Number;
     return ss.str();
  }

string LTS(vector<int> l) {
    string a = "";
    for(int i=0; i<l.size(); i++) {
        if(l[i] > 0) {
            a+=  NumberToString(l[i]);
        }
    }
    return a;
}

string compute(ll next) {
    vector<int> myList = NOL(next);
    for(int i=(int)myList.size()-1; i>0; i--) {
        int t = myList[i];
        int p = myList[i-1];
        if(p > t) {
            for(int k=i; k < myList.size(); k++) {
                myList[k] = 9;
            }
            myList[i-1] --;
        }

    }
    return LTS(myList);
}

int main() {
    int c = 1;
    int t;
    ifstream fin("B-large.in");
    ofstream fout("small.out");
    fin>>t;
    while(t--) {
        ll next;
        fin>>next;

        fout<<"Case #"<<c<<": ";
        string res = compute(next);
        fout<<res<<endl;
        c++;
    }

    return 0;
}
