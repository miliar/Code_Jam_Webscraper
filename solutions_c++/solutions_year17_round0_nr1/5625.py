#include<iostream>
#include<string>

using namespace std;

int main()
{
    int T, K, pos, cont = 0, temp;
    string S;
    cin >> T;
    for( int i = 0; i < T; i++)
    {
        cin >> S;
        cin >> K;
        // cout << "S:" << S << ", K: " << K << endl;
        pos = S.find("-");
        if(pos == string::npos)
        {
            cout << "Case #" << i + 1 << ": 0" << endl;
        }
        else
        {
                    // cout << "Condicinal pos + K: " << pos + K << endl;
                    // cout << "Condicional size: " << S.size() << endl;
            
            if ( (pos + K) <= S.size() )
            {
                while( pos != string::npos)
                {
                    // cout << "\nIniciando npos, Numero "<< i << ": " << S << endl;
                    temp = pos + K;
                    // cout << "pos + K: " << pos + K << endl;
                    // cout << "size: " << S.size() << endl;
                    //     cout << S << endl;
                    while(pos < temp)
                    {

                        if(S[pos] == '-')
                            S.replace(pos,1,"+");
                        else
                            S.replace(pos,1,"-");
                        
                        pos++;
                        // cout << S << endl;
                    }
                    cont++;
                    // cout << "Contador: " << cont << endl;
                    // cout << S << endl;
                    pos = S.find("-");
                    // cout << "pos final : " << pos << endl;
                    // cout << "pos + K final : " << pos + K << endl;
                    // cout << "size final: " << S.size() << endl;
                    if ( (pos + K) > S.size() )
                    {
                        break;
                    }
                }
                if ( (pos + K) > S.size() )
                {
                    cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
                }
                else
                {
                    cout << "Case #" << i + 1 << ": " << cont << endl;
                }
            }
            else
            {
                cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
            }

        }
        cont = 0;
    } 

    return 0;
}