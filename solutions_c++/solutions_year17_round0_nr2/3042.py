
#include<iostream>

using namespace std;

int testy;
string n;

bool czyok(string &n) {
    bool ok = true;
    for (int i=0; i<n.length()-1; ++i) {
        if (n[i+1]<n[i]) {ok=false; break;}
    }
    return ok;
}

int main()
{
    cin>>testy;

    for (int t=1; t<=testy; ++t) {
        cin>>n;
        //jak jest ok to n
        //jak nie, to musimy zmniejszyæ któr¹œ cyfrê - próbujemy od prawej
        //zawsze zmniejszenie o 1 starczy bo musia³a byæ wiêksza od nast
        //a teraz mo¿na potem same 9'ki
        if (czyok(n)) {
                string k;
                int j=0;
                while (n[j]=='0') ++j;
                while (j<n.length()) {k+=n[j]; j++;}
                cout<<"Case #"<<t<<": "<<k<<"\n";
                continue;
            }
        for (int i=n.length()-1; i>=0; --i) {

            if (n[i]=='0') continue;
            n[i]--;
            for (int j=i+1; j<n.length(); ++j) n[j]='9';
            if (czyok(n)) {
                string k;
                int j=0;
                while (n[j]=='0') ++j;
                while (j<n.length()) {k+=n[j]; j++;}
                cout<<"Case #"<<t<<": "<<k<<"\n";
                break;
            }
        }
    }


    return 0;
}
