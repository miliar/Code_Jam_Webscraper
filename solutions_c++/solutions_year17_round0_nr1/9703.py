#include <iostream>
#include <fstream>

#include <vector>
using namespace std;
int main() {
    int n;
    cin>>n;
    vector <string> a;
    vector <int> b;
    for(int i=0;i<n;i++)
    {
        string t;
        int s;
        cin>>t;
        cin>>s;
        a.push_back(t);
        if(s>t.size())
        {
            b.push_back(-1);
        } else{


     for(int j=0;j<=a[i].size()-s;j++) {
         b.push_back(0);
         if (a[i][j] == '-') {
             a[i][j] = '+';
             ++b[i];
             for (int z = 1; z < s; z++) {
                 if (a[i][j + z] == '-') {
                     a[i][j + z] = '+';
                 } else {
                     a[i][j + z] = '-';
                 }
             }

         }
     }
        for(int j=0;j<a[i].size();j++)
        {
            if(a[i][j]=='-') {
                b[i] = -1;
            }
        }



    } }
    for(int i=0;i<n;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        if(b[i]==-1)
        {
            cout<<"IMPOSSIBLE\n";
        } else{
            cout<<b[i]<<endl;
        }

    }

    return 0;
}
