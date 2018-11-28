#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);
    int t;
    cin >> t;
    for(int i=0; i<t; i++){
        string pan;
        int k, count=0, flag=1;
        cin >> pan >> k;
        for(int j=0; j<pan.size(); j++){
            if(pan[j]=='-'){
                    count++;
                for(int x=j; x<j+k; x++){
                    if(j+k>pan.size()){
                        break;
                    }
                    if(pan[x]=='-'){
                        pan[x]='+';
                    } else {
                        pan[x]='-';
                    }
                }

            }
        }
        for(int y=0; y<pan.size(); y++){
            if(pan[y]=='-'){
                flag=0;
                cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
                break;
            }
        }
        if(flag==1){
            cout << "Case #" << i+1 << ": " << count << endl;
        }
    }
    fclose (stdin);
    fclose (stdout);
    return 0;
}
