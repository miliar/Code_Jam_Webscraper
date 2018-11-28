#include<iostream>
#include<string>

using namespace std;

int main()
{
    int T;
    cin >> T;
    string num;

    long long n, temp, numero;
    bool listo = false;

    size_t sz;
    
    for (int i = 0; i < T; i++)
    {
        cin >> n;
        // cout << "N de entrada" << n << endl;
        while( listo == false )
        {
            // cout << "Hola entre con " << n << endl;
            num = to_string(n);
            // cout << n << endl;
            string a = "a", b = "b";  
            // cout << "a < b " << (a.compare(b)) << endl;
            // cout << "a > b " << (b.compare(a)) << endl;
            // cout << "a = a " << (a.compare(a)) << endl;
            // cout << "num " << num << " " << num.compare(0,1,num,1,1) << endl;
            for(int l = 0; l < num.size() ; l++)
            {
                for(int j = 0; j < num.size()-1 ; j++)
                {
                    if( num.compare(j,1,num,j+1,1) > 0 )
                    {
                        // cout << num[j] << " mayor " << num[j+1] << endl;
                        num[j]--;
                        // cout << "num --" << num << endl;
                        // cout << "k " << j+1 << " size: " << num.size() << endl;
                        for (int k = j+1; k < num.size(); k++)
                        {
                            // cout << "entre " << endl;
                            num[k] = '9'; 
                            // num.replace(k,1,"9"); 
                            // cout << "num cambiado" << num  << endl;
                        }
                        // cout << "num nuevo" << num  << endl;
                        // cout << "tengo el numero nuevoooooo" << endl;
                        break;
                    }
                }
            }
            listo = true;
        }
        numero = stoll(num,&sz);
        // cout << "numero " << numero << endl;
        cout << "Case #" << i+1 << ": " << numero << endl;
        listo = false;


    }

    return 0;
}