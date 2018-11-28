#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

int main()
{
    int t;
    string n;
    cin>>t;
    for(int x=0; x<t; ++x){
        cin>>n;
        int pos = 1;
        while(pos<n.size()){
            if(n[pos-1]>n[pos])
                break;
            pos++;
        }
        if(pos!=n.size()){
            while(--pos>0){
                if(n[pos-1]<n[pos])
                    break;
            }
            n[pos++]--;
            while(pos<n.size()){
                n[pos++] = '9';
            }
        }
        int ansPos = 0;
        for(int ansSize=n.size(); ansPos<ansSize-1; ansPos++){
            if(n[ansPos]!='0')
                break;
        }
        cout<<"Case #"<<x+1<<": "<<n.substr(ansPos)<<endl;
    }
    return 0;
}
