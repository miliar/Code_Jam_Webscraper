#include<bits/stdc++.h>
using namespace std ;
#define LL long long

void make(char a[][26] , int sr,int er , int sc , int ec , char x ){

for(int i=sr ; i<=er ; i++){
    for(int j=sc ; j<=ec ; j++){
        a[i][j]=x ;
    }
}

}

int main()
{

 int t ;
 cin>>t ;
 int f=1 ;
 while(f<=t){
    int r , c ;
    cin>>r>>c ;
    vector<pair<int,int> > v ;
    char a[r+1][26] ;
    for(int i=1 ; i<=r ; i++){
        for(int j=1 ; j<=c ; j++){
            cin>>a[i][j] ;
            if(a[i][j]!='?'){
                v.push_back(make_pair(i,j)) ;
            }
        }
    }
    sort(v.begin() , v.end()) ;

       int sr,er,sc,ec ;
        int k ;
        int currr , currc, nextr , nextc ;
        int prevc=1 , prevr=1 ;
        for(int i=0 ; i<v.size() ; i++){
            currr=v[i].first ;
            k=i+1 ;
            nextr=-1 ;
            while(k<v.size()){
                if(v[k].first>currr){
                    nextr=v[k].first ;
                    break ;
                    }
                k++ ;
            }
            if(nextr==-1){
                nextr=r+1 ;
            }
            sr=currr ;
            er=nextr-1 ;
            sc=prevc ;
            if(i+1!=k){
            ec=v[i].second ;

            }
            else{
                ec=c ;
            }
            make(a , sr,er,sc,ec,a[v[i].first][v[i].second]) ;
            prevc=ec+1 ;
            if(prevc>c){
                prevc=1 ;
            }
        }

        if(v[0].first>1){

                int gg ;
                gg=v[0].first ;

                gg-- ;
                for(int q=gg ; q>=1 ; q--)
                {
                    for(int h=1 ; h<=c ; h++){
                        a[q][h]=a[q+1][h] ;
                    }
                }

        }
    cout<<"Case #"<<f<<":"<<endl ;
    for(int i=1 ; i<=r ; i++){
        for(int j=1 ; j<=c ; j++){
            cout<<a[i][j] ;
        }
        cout<<endl ;
    }
    f++ ;
 }
 return 0 ;
}
