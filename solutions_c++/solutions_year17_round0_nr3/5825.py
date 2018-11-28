#include<iostream>
#include<string>
#include <forward_list>
#include<math.h>

using namespace std;

int main()
{
    int T;
    cin >> T;
    long long n, k, cont; 
    forward_list<long long> sillas;
    
    for (int y = 0; y < T; y++)
    {
        cin >> n >> k;

        for (long long i = 1; i <= k ; i++)
        {
            // cout << "persona " << i << endl;
            // cout << "n es: " << n << endl;
            // cout << "Lista Inicial: " ;
            // for(long long &x:sillas) cout << x << " ";
            // cout << endl;
            if( n % 2 == 0)
            {
                sillas.push_front( n / 2 );
                sillas.push_front( (n / 2) - 1 );
                // cout << "Es Par" << endl;
                // for(long long &x:sillas) cout << x << " ";
                // cout << endl;
            }else
            {
                sillas.push_front( n / 2 );
                sillas.push_front( n / 2 );
                // cout << "Es impar" << endl;
                // for(long long &x:sillas) cout << x << " ";
                // cout << endl;
            }
            // cout << "N. persona: " << i+1 << endl;
            // cout << "Sin ordenar: ";
            // cout << "Lista despues: " ;
            // for(long long &x:sillas) cout << x << " ";
            // cout << endl;

            
            if( i == k )
            {
                if( n % 2 == 0)
                {
                    cout << "Case #" << y+1 << ": " << n/2 << " " << (n / 2) -1 << endl;
                }else
                {
                    cout << "Case #" << y+1 << ": " << n/2 << " " << n / 2 << endl;
                }
            }
            else
            {
                sillas.sort( greater<long long>() );
                // cout << "Ordenada: ";
                // for(long long &x:sillas) cout << x << " ";
                // cout << endl;
                
                n = sillas.front();
                sillas.pop_front();
                // cout << "Sin el ultimo: ";
                // for(long long &x:sillas) cout << x << " ";
                // cout << "\nN Ahora es: "<< n << endl << endl << endl;

            }
        }
        // cout << "\n------------------" << endl;
        sillas.clear();
        // for(long long &x:sillas) cout << x << " ";
        // cout << endl << "---------------------------------" << endl;

        // for(long long &x: sillas) cout << " " << x;
        // cout << endl;

        // sillas.sort(greater<long long>());
        // for(long long &x: sillas) cout << " " << x;
        // cout << endl << endl;
        
//         4 2
// 5 2
// 6 2
// 10 5
// 20 7
// 30 4
// 20 17

    }

    return 0;
}

// 1 | O 0 - O | 1 0  
// 2 | O O 0 O | 0 0 

// 1 | O - 0 - O | 1 1
// 2 | O 0 O - O | 0 0
// 3 | O O O 0 O | 0 0

// 1 | O - 0 - - O | 2 1 
// 2 | O - O 0 - O | 1 0
// 3 | O 0 O O - O | 0 0
// 4 | O O O O 0 O | 0 0

// 1 | O - - 0 - - O | 2 2  
// 2 | O 0 - O - - O | 1 0 
// 3 | O O - O 0 - O | 1 0
// 4 | O O 0 O O - O | 0 0
// 5 | O O O O O 0 O | 0 0

// 1 | O - - 0 - - - O | 3 2 
// 2 | O - - O - 0 - O | 1 1
// 3 | O 0 - O - O - O | 1 0
// 4 | O O 0 O - O - O | 0 0
// 5 | O O O O 0 O - O | 0 0
// 6 | O O O O O O 0 O | 0 0

// 1 | O - - - 0 - - - O | 3 3 
// 2 | O - 0 - O - - - O | 1 1
// 3 | O - O - O - 0 - O | 1 1
// 4 | O 0 O - O - O - O | 0 0
// 5 | O O O 0 O - O - O | 0 0
// 6 | O O O 0 O 0 O - O | 0 0
// 7 | O O O 0 O 0 O 0 O | 0 0

// 1 | O - - - 0 - - - - O | 4 3 
// 2 | O - - - O - 0 - - O | 2 1
// 3 | O - 0 - O - O - - O | 1 1
// 4 | O - O - O - O 0 - O | 1 0
// 5 | O 0 O - O - O O - O | 0 0
// 6 | O O O 0 O - O O - O | 0 0
// 7 | O O O O O 0 O O - O | 0 0
// 8 | O O O O O O O O 0 O | 0 0

// 1 | O - - - - 0 - - - - O | 4 4
// 2 | O - 0 - - O - - - - O | 2 1
// 3 | O - O - - O - - 0 - O | 2 1
// 4 | O - O 0 - O - - O - O | 1 0
// 5 | O - O O - O 0 - O - O | 1 0
// 6 | O 0 O O - O O - O - O | 0 0
// 7 | O O O O 0 O O - O - O | 0 0
// 8 | O O O O O O O 0 O - O | 0 0
// 9 | O O O O O O O O O 0 O | 0 0

//  1 | O - - - - 0 - - - - - O | 5 4 
//  2 | O - - - - O - - 0 - - O | 2 2
//  3 | O - 0 - - O - - O - - O | 2 1
//  4 | O - O 0 - O - - O - - O | 1 0
//  5 | O - O O - O 0 - O - - O | 1 0
//  6 | O - O O - O O - O 0 - O | 1 0
//  7 | O 0 O O - O O - O O - O | 0 0
//  8 | O O O O 0 O O - O O - O | 0 0
//  9 | O O O O O O O 0 O O - O | 0 0
// 10 | O O O O O O O O O O 0 O | 0 0

//  1 | O - - - - - - - - - 0 - - - - - - - - - - O | 10 9
//  2 | O - - - - - - - - - O - - - - 0 - - - - - O | 5 4
//  3 | O - - - - 0 - - - - O - - - - O - - - - - O | 4 4
//  4 | O - - - - O - - - - O - - - - O - - 0 - - O | 2 2
//  5 | O - 0 - - O - - - - O - - - - O - - O - - O | 2 1
//  6 | O - O - - O - 0 - - O - - - - O - - O - - O | 2 1
//  7 | O - O - - O - O - - O - 0 - - O - - O - - O | 2 1 --------- 7
//  8 | O - O 0 - O - O - - O - O - - O - - O - - O | 1 0
//  9 | O - O O - O - O 0 - O - O - - O - - O - - O | 1 0
// 10 | O - O O - O - O O - O - O 0 - O - - O - - O | 1 0
// 11 | O - O O - O - O O - O - O O - O 0 - O - - O | 1 0
// 12 | O - O O - O - O O - O - O O - O O - O 0 - O | 1 0
// 13 | O 0 O O - O - O O - O - O O - O O - O O - O | 0 0
// 14 | O O O O 0 O - O O - O - O O - O O - O O - O | 0 0
// 15 | O O O O O O 0 O O - O - O O - O O - O O - O | 0 0
// 16 | O O O O O O O O O 0 O - O O - O O - O O - O | 0 0
// 17 | O O O O O O O O O O O 0 O O - O O - O O - O | 0 0
// 18 | O O O O O O O O O O O O O O 0 O O - O O - O | 0 0
// 19 | O O O O O O O O O O O O O O O O O 0 O O - O | 0 0
// 20 | O O O O O O O O O O O O O O O O O O O O 0 O | 0 0

//  1 | O - - - - - - - - - - - - - - 0 - - - - - - - - - - - - - - - O | 15 14
//  2 | O - - - - - - - - - - - - - - O - - - - - - - 0 - - - - - - - O | 7 7
//  4 | O - - - - - - 0 - - - - - - - O - - - - - - - O - - - - - - - O | 7 6
//  5 | O - - - - - - O - - - 0 - - - O - - - - - - - O - - - - - - - O | 3 3
//  3 | O - - - - - - O - - - O - - - O - - - 0 - - - O - - - - - - - O | 3 3
//  6 | O - - - - - - O - - - O - - - O - - - O - - - O - - - 0 - - - O | 3 3
//  7 | O - - 0 - - - O - - - O - - - O - - - O - - - O - - - O - - - O | 3 2
//  8 | O - - O - 0 - O - - - O - - - O - - - O - - - O - - - O - - - O | 1 1
//  9 | O - - O - O - O - 0 - O - - - O - - - O - - - O - - - O - - - O | 1 1
// 10 | O - - O - O - O - O - O - 0 - O - - - O - - - O - - - O - - - O | 1 1
// 11 | O - - O - O - O - O - O - O - O - 0 - O - - - O - - - O - - - O | 1 1
// 12 | O - - O - O - O - O - O - O - O - O - O - 0 - O - - - O - - - O | 1 1
// 13 | O - - O - O - O - O - O - O - O - O - O - O - O - 0 - O - - - O | 1 1
// 14 | O - - O - O - O - O - O - O - O - O - O - O - O - O - O - 0 - O | 1 1
// 15 | O 0 - O - O - O - O - O - O - O - O - O - O - O - O - O - O - O | 1 0
// 16 | O O 0 O - O - O - O - O - O - O - O - O - O - O - O - O - O - O | 0 0
// 17 | O O O O 0 O - O - O - O - O - O - O - O - O - O - O - O - O - O | 0 0
// 18 | O O O O O O 0 O - O - O - O - O - O - O - O - O - O - O - O - O | 0 0
// 19 | O O O O O O O O 0 O - O - O - O - O - O - O - O - O - O - O - O | 0 0
// 20 | O O O O O O O O O O 0 O - O - O - O - O - O - O - O - O - O - O | 0 0
// 21 | O O O O O O O O O O O O 0 O - O - O - O - O - O - O - O - O - O | 0 0
// 22 | O O O O O O O O O O O O O O 0 O - O - O - O - O - O - O - O - O | 0 0
// 23 | O O O O O O O O O O O O O O O O 0 O - O - O - O - O - O - O - O | 0 0
// 24 | O O O O O O O O O O O O O O O O O O 0 O - O - O - O - O - O - O | 0 0
// 25 | O O O O O O O O O O O O O O O O O O O O 0 O - O - O - O - O - O | 0 0
// 26 | O O O O O O O O O O O O O O O O O O O O O O 0 O - O - O - O - O | 0 0
// 27 | O O O O O O O O O O O O O O O O O O O O O O O O 0 O - O - O - O | 0 0
// 28 | O O O O O O O O O O O O O O O O O O O O O O O O O O 0 O - O - O | 0 0
// 29 | O O O O O O O O O O O O O O O O O O O O O O O O O O O O 0 O - O | 0 0
// 30 | O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O 0 O | 0 0

