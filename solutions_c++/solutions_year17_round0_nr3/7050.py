#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <random>

using namespace std;


class Stalls {

    private:

    int m_n_stall ; 
    vector<bool> m_stalls ;
    
    vector<int> m_left ;
    vector<int> m_right ;
    vector<int> m_min ;
    vector<int> m_max ;
    
    void update() {
    
        int n_l = 0 ;
        int n_r = 0 ;
        
        for (int i = 0 ; i < m_n_stall ; i++)
        {

            int j = m_n_stall-1-i ;
        
            if ( m_stalls[i] ) n_l = 0 ; else n_l = n_l + 1 ;
            m_left[i] = n_l ; 
            
            if ( m_stalls[j] ) n_r = 0 ; else n_r = n_r + 1 ;
            m_right[j] = n_r ;
                           
        }    
    
        for (int i = 0 ; i < m_n_stall ; i++)
        {
            m_min[i] = m_left[i] ;
            m_max[i] = m_left[i] ;
            
            if (m_right[i] < m_min[i]) m_min[i] = m_right[i] ;
            if (m_right[i] > m_max[i]) m_max[i] = m_right[i] ;
                           
        }
    
    }
    
    int choose(){
    
        int idx = 0 ;
        int min = 0 ;
        int max = 0 ; 
        
        for (int i = 0 ; i < m_n_stall ; i++)
        {
            
            if (m_min[i] > min) {
                min = m_min[i] ;
                max = m_max[i] ;
                idx = i ;
            }
            if (m_min[i] == min) {
                if (m_max[i] > max)
                {
                    max = m_max[i] ;
                    idx = i ;
                }
            }
                           
        }
        
        
        return idx ;
    
    }

    public: 
    
    Stalls(int n_stall){
    
        m_n_stall = n_stall + 2 ; 
        
        m_stalls = vector<bool>(m_n_stall,false) ;
        
        m_stalls[0] = true ;
        m_stalls[m_n_stall-1] = true ;
        
        m_left  = vector<int>(m_n_stall,0) ;
        m_right = vector<int>(m_n_stall,0) ;
        m_min = vector<int>(m_n_stall,0) ;
        m_max = vector<int>(m_n_stall,0) ;
        update() ; 
        
    }
    
    
    void print(){

        for (int i =0 ; i < m_stalls.size() ; i++)
        {
            if ( m_stalls[i] ) cerr << "x" ; else cerr << "°" ;
        }
        cerr << endl ;
        
        for (int i =0 ; i < m_stalls.size() ; i++)
        {
            cerr << m_min[i] ; 
        }
        cerr << endl ;
        
        for (int i =0 ; i < m_stalls.size() ; i++)
        {
            cerr << m_max[i] ; 
        }
        cerr << endl ;
        
        cerr << endl ; 
    
    }
    
    pair<int,int> newcomer() {
    
        int idx = choose() ;
        // cerr << "choose " << idx << endl ;
        m_stalls[idx] = true ;
        
        int min = m_min[idx] ;
        int max = m_max[idx] ;
        
        update() ;
        
        pair<int,int> p(max-1,min-1) ;
        // cerr << "(" << max << "," << min << ")" << endl ;
        return p ; 
    
    }


} ;



int main()
{

    int nb_tests ;
    cin >> nb_tests ;
               
    for (int i = 0; i < nb_tests; ++i)
    {
        
        // read shit
        int n_stall, n_people ;           
        cin >> n_stall ;
        cin >> n_people ;
        
             
        // build Stalls
        Stalls stalls = Stalls(n_stall) ;
        // stalls.print() ;
        
        // rush hour
        
        pair<int,int> max_min ; 
        
        for (int p = 0; p < n_people; ++p)
        {
            max_min = stalls.newcomer() ;
            // stalls.print() ;
        }
        
        
        // write shit
        cout << "Case #" << i+1 << ": " ;
        cout << max_min.first << " " << max_min.second << endl ;
                
    }




    return 0;
}

