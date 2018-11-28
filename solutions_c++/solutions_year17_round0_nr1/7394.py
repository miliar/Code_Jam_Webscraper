#include <iostream>
#include <string>

using namespace std;



int main()
{
    std::ios::sync_with_stdio(false);
    int t,T;
    cin >> T;
    for (t=0; t<T; t++)
    {
        int ans = 0,k;
        string s;
        cin>>s>>k;
        for (int i=0; i<(s.size()-k+1); i++) {
            if(s[i]=='-')
            {
                ans++;
                for (int j=0; j<k; j++) {
                    if (s[i+j] == '-') {
                        s[i+j] = '+';
                    }
                   else{
                       s[i+j] = '-';
                   }
               }
                //cout<<"Testing:: " << i<<" :: " << s<<endl;
            }
        }
        string toComp(s.size(),'+');
        if(s==toComp)
            cout <<"Case #"<<t+1<<": "<< ans <<endl;
        else
            cout <<"Case #"<<t+1<<": "<< "IMPOSSIBLE" <<endl;
    }
    return 0;
}

