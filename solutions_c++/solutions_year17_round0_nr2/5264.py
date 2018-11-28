#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int t;
    cin >> t;
    for(int i=0;i<t;i++){
        string n;
        cin >> n;
        int j=0;
        int flag=0;
        while(j<n.length()-1){
            int flag2=0,flag3=0;
            if(n[j]<=n[j+1]){           //comparing characters would be same as comparing the numbers
                j++;
            }
            else{
                int k=j+1;
                while(k!=n.length()){
                    n[k]='9';
                    k++;
                }
                if(n[j]!='0' && (n[j]!='1' || j!=0)){
                    n[j]--;
                    flag3=1;
                    if(n[j]<n[j-1]){
                        j--;
                        flag2=1;
                        //keep the outer while loop going           
                    }
                }
                else if(n[j]=='0'){
                    while(j>0){
                        if(n[j]==0){
                            j--;
                        }
                        else{
                            n[j]--;
                            break;
                        }
                    }
                }
                if(flag2==0){
                    if(n[j]=='1' && j==0 && flag3==0){
                        //length of string decreases
                        cout << "Case #" << i+1 <<": "<< n.substr(1,n.length()-1)<<endl;
                        flag=1;
                        break; 
                    }
                    cout << "Case #" << i+1 <<": "<< n << endl;
                    flag=1;
                    break;
                }
            }
        }
        if(flag==0)
            cout << "Case #" << (i+1) <<": "<< n << endl;
    }
  return 0;
}
