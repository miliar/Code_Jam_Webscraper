#include<bits/stdc++.h>
using namespace std ;


int main()
{
    freopen("C-small-1-attempt0.in","r", stdin);
    freopen("C-outdar.out", "w", stdout);
    int test ;
    cin>>test ;
    int z=1 ;
    while(test--)
    {
        int n,p ;
        cin>>n>>p ;
        vector<int>arr ;
        for(int i=0; i<=n+1 ; i++)
        {
            arr.push_back(0) ;
        }
        arr[0]=1 ;
        arr[n+1]=1 ;
        vector< pair<int,int> >minV ;
        for(int x=1 ; x<=p ; x++)
        {
            minV.clear() ;
            int currMin = -1 ;
            for(int i=1 ; i<n+1 ; i++)
            {
                if(arr[i]==0)
                {
                    int cL=0 ;
                    for(int j=i-1 ; j>0 ; j--)
                    {
                        if(arr[j]==0)
                        {
                            cL++ ;
                        }
                        else
                        {
                            break ;
                        }
                    }

                    int cR=0 ;
                    for(int k=i+1 ; k<n+1 ; k++)
                    {
                        if(arr[k]==0)
                        {
                            cR++ ;
                        }
                        else
                        {
                            break ;
                        }
                    }
                    int minC = min(cL, cR) ;
                    if(minC>currMin)
                    {
                        currMin = minC ;
                        minV.clear() ;
                        minV.push_back(make_pair(-1*max(cL,cR),i)) ;
                    }
                    else if(minC==currMin)
                    {
                        minV.push_back(make_pair(-1*max(cL,cR),i)) ;
                    }
                }
            }
            if(minV.size()==1)
            {
                //cout << minV[0].second << " " ;
                arr[minV[0].second] = 1 ;
            }
            else
            {
                sort(minV.begin(), minV.end()) ;
                //cout << minV[0].second << " " ;
                arr[minV[0].second] = 1 ;
            }
        }
        //cout << minV[0].first << " ";
        int r = minV[0].second ;
        int pL=0 , pR=0 ;
        for(int i=r-1 ; i>0 ; i--)
        {
            if(arr[i]==0)
            {
                pL++ ;
            }
            else
            {
                break ;
            }
        }
        for(int i=r+1 ; i<n+1 ; i++)
        {
            if(arr[i]==0)
            {
                pR++ ;
            }
            else
            {
                break ;
            }
        }
        cout << "Case #" << z << ": " ;
        cout << max(pL,pR) << " " << min(pL,pR) << endl ;
        z++ ;
    }
}
