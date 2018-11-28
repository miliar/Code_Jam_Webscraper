#include<iostream>

using namespace std;

int testy;
string napis;
int k;

int main()
{
    ios_base::sync_with_stdio(0);

    cin>>testy;

    for(int t=1; t<=testy; ++t) {
        cin>>napis>>k;
        int licznik = 0;
        for (int i=0; i<napis.length()+1-k; ++i) {
            if (napis[i]=='-') {
                for (int j=i; j<i+k; ++j) {
                    if (napis[j]=='-') napis[j]='+';
                    else napis[j]='-';
                }
                ++licznik;
            }
        }
        bool ojej = false;
        for (int i=0; i<napis.length(); ++i) {
            if (napis[i]=='-') {ojej = true; break; }
        }
        cout<<"Case #"<<t<<": ";
        if (ojej) cout<<"IMPOSSIBLE"; else cout<<licznik;
        cout<<"\n";
    }

    return 0;
}
