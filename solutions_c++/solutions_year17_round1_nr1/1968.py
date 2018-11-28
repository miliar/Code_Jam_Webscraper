#include <iostream>
#include <vector>
#include <queue>

using namespace std ;


const int maxR = 30 ;

int R, C ;
bool seen[maxR] ;
char letters[maxR] ;
int leftest[maxR], rightest[maxR], topmost[maxR], bottom[maxR] ;
vector<string> grid(maxR) ;


void fill_up(char ch, int r1, int c1, int r2, int c2)
{
    for(int i = r1 ; i <= r2 ; i++)
        for(int j = c1 ; j <= c2 ; j++)
            grid[i][j] = ch ;
}

bool isEmpty(int r1, int c1, int r2, int c2)
{
    for(int i = r1 ; i <= r2 ; i++)
    {
      //  cout << grid[i] << "\n" ;
        for(int j = c1 ; j <= c2 ; j++)
            if(grid[i][j] != '?')
                return false ;
    }
    return true ;
}

void solve()
{
    for(int i = 0 ; i < maxR ; i++)
    {
        topmost[i] = bottom[i] = leftest[i] = rightest[i] = -1 ;
        seen[i] = false ;
    }
    
    cin >> R >> C ;
    
    for(int i = 0 ; i < R ; i++)
        cin >> grid[i] ;
    
  //  for(int i = 0 ; i < R ; i++)
    //    cout << grid[i] << "\n" ;
    
    char ch ;
    int tot = 0 ;
    for(int i = 0 ; i < R ; i++)
        for(int j = 0 ; j < C ; j++)
        {
            ch = grid[i][j] ;
            
            if(ch == '?')
                continue ;
            
            if(!seen[(int)(ch-'A')])
            {
                seen[(int)(ch-'A')] = true ;
                letters[tot] = ch ;
                tot++ ;
            }
        }
    
    for(int k = 0 ; k < tot ; k++)
        for(int i = 0 ; i < R ; i++)
            for(int j = 0 ; j < C ; j++)
                if(grid[i][j] == letters[k])
                {
                    if(topmost[k] == -1 || i < topmost[k])
                        topmost[k] = i ;
                    if(bottom[k] == -1 || i > bottom[k])
                        bottom[k] = i ;
                    if(leftest[k] == -1 || j < leftest[k])
                        leftest[k] = j ;
                    if(rightest[k] == -1 || j > rightest[k])
                        rightest[k] = j ;
                }
    
    
    for(int k = 0 ; k < tot ; k++)
        fill_up(letters[k], topmost[k], leftest[k], bottom[k], rightest[k]) ;
    
    int b, t, l, r ;
    for(int k = 0 ; k < tot ; k++)
    {
        t = topmost[k] ;
        l = leftest[k] ;
        r = rightest[k] ;
        
        while(t > 0 && isEmpty(t-1, l, t-1, r))
        {
            fill_up(letters[k], t-1, l, t-1, r) ;
            t-- ;
            topmost[k]-- ;
        }
    }
    
    for(int k = 0 ; k < tot ; k++)
    {
        b = bottom[k] ;
        l = leftest[k] ;
        r = rightest[k] ;
        
        while(b < R-1 && isEmpty(b+1, l, b+1, r))
        {
            fill_up(letters[k], b+1, l, b+1, r) ;
            b++ ;
            bottom[k]++ ;
        }
    }
    
    for(int k = 0 ; k < tot ; k++)
    {
        t = topmost[k] ;
        l = leftest[k] ;
        b = bottom[k] ;
        
        while(l > 0 && isEmpty(t, l-1, b, l-1))
        {
            fill_up(letters[k], t, l-1, b, l-1) ;
            l-- ;
            leftest[k]-- ;
        }
    }
    
    for(int k = 0 ; k < tot ; k++)
    {
        t = topmost[k] ;
        r = rightest[k] ;
        b = bottom[k] ;
        
        while(r < C-1 && isEmpty(t, r+1, b, r+1))
        {
            fill_up(letters[k], t, r+1, b, r+1) ;
            r++ ;
            rightest[k]++ ;
        }
    }
    
    for(int i = 0 ; i < R ; i++)
        cout << grid[i] << "\n" ;
}

int main()
{
    ios::sync_with_stdio(false) ;
    cin.tie(0) ;
    
    int T ;
    cin >> T ;
    
    for(int i = 1 ; i <= T ; i++)
    {
        cout << "Case #" << i << ":\n" ;
        solve() ;
    }
    
    
    return 0 ;
}