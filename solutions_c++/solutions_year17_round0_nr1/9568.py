#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

char gira2 (char& a){
    return (a=='-'? '+' : '-');
}

void gira (char S[], int first, const int last, const int k, int & contatore, int livello){
    //cout << first << " " << k << " " << last << endl;
    int j = 0;
    /*
    while (S[j] != '\0') {
        cout << S[j];
        j++;
    }
    */
    //getchar();
    //cout << endl;
    if (first+k <= last) {
        if (S[first] == '-'){
            contatore++;

            for (int i = 0; i<k; i++){
                S[first+i] = gira2 (S[first+i]);
            }
        }
        gira (S, first+1, last, k, contatore,livello+1);
    }
    //cout<<"chiudo livello " <<livello<<endl;
}

int main()
{
    ifstream myin ("input.txt");
    ofstream myout ("output.txt");
    int T;
    myin >> T;

    for (int h = 1; h<=T; h++){
        char S[1005];
        int k;
        myin >> S;
        myin >> k;
        int first = 0;
        S[sizeof(S)] = '\0';
        int last = strlen(S);
        int j = 0;
        /*
        while (S[j] != '\0') {
            cout << S[j];
            j++;
        }
        cout << endl;
        */
        int contatore = 0;

        gira (S, first, last, k, contatore,0);


        j = 0;
        bool impossibile = false;
        while (S[j] != '\0' && !impossibile) {
            if (S[j] == '-'){
                impossibile = true;
            }
            else j++;
        }
        myout << "Case #" << h << ": " ;

        if (impossibile){
            myout << "IMPOSSIBLE" << endl;
        }
        else    {
            myout << contatore << endl;
        }

    }

    return 0;
}
