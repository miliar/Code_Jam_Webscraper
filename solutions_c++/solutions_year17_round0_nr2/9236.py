#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string liczba;
int l[20];

void wymaksuj(int j) {
    for(int i = j; i < liczba.length(); i++) {
        l[i] = 9;
    }
}

int main() {
    int n;

    cin>>n;



    for(int i = 1; i <= n; i++) {
        cin>>liczba;

        if(liczba.length() == 1) {
            cout<<"Case #"<<i<<": "<<liczba<<endl;
            continue;
        }

        for(int j = 0; j < liczba.length(); j++) {
            l[j] = liczba[j] - '0';
        }

        for(int j = liczba.length() - 1; j > 0; j--) {
            int cyfra1 = l[j];
            int cyfra2 = l[j - 1];

            if(cyfra1 < cyfra2) {
                l[j - 1]--;
                wymaksuj(j);
            }
        }

        cout<<"Case #"<<i<<": ";

        long long wynik = 0;
        for(int j = 0; j < liczba.length(); j++) {
            wynik = wynik*10 + l[j];
        }

        cout<<wynik<<endl;
    }
}
