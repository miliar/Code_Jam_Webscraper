#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <random>

using namespace std;


int main()
{

    // read shit

    int nb_numbers ;
    cin >> nb_numbers ;

    // get numbers
    
    vector<vector<int>> numbers ;
    for (int i = 0; i < nb_numbers; ++i)
    {
        long int n ;        
        cin >> n ;
        
        long int decad = 1 ;
        
        vector<int> flush ;
        for (int p = 1 ; p < 20 ; ++p)
        {
           decad = decad * 10 ;
           long int k = n%decad ;
           k = k / (decad/10) ;
           
           flush.push_back(k) ;
           
           if (n / decad == 0) break ; 
           
        }
        
        numbers.push_back(flush) ;
        
    }


    vector<int>::iterator it ;
    vector<int>::reverse_iterator rit ;
    

    // assess shit
    for (int i = 0; i < nb_numbers; ++i)
    {
        
        int rank_1 = 0 ; 
        int rank_2 = 0 ;
        
        if (numbers[i].size() != 1) 
        {
            for (int r = 0 ; r < numbers[i].size() - 1 ; r++ )
            {
                if (numbers[i][r] < numbers[i][r+1] ) 
                {
                    rank_1 = r+1 ;
                    rank_2 = r+1 ;
                }
                if (numbers[i][r] == numbers[i][r+1] ) 
                {
                    rank_2 = r+1 ;
                } 
                
            } 
        }

        cerr << i+1 << " : " << rank_1 << "," << rank_2 << endl ;
        
                
        if (rank_1 != 0)
        {

            numbers[i][rank_2] =  numbers[i][rank_2] - 1 ; 
            for (int r = rank_2-1 ; r >=0 ; r-- )
            {
                numbers[i][r] = 9 ; 
            } 
        }
        
    }


    // write shit
    
    for (int i = 0; i < nb_numbers; ++i)
    {
        cout << "Case #" << i+1 << ": " ;
        
        int count = 0 ; 
        for (rit = numbers[i].rbegin() ; rit != numbers[i].rend() ; rit++)
        {
            if ( *rit != 0 || count !=0 ) cout << (*rit) ;
            count++ ;
            
        }        
        cout << endl ; 
    }

    
    // try_all_the_things(videos_size, requests, endpoints, caches);

    return 0;
}

