#include<iostream>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
using namespace std;
int R,C;
char cake[26][26];
bool v[26][26];
int mover[4]={1,0,-1,0};
int movec[4]={0,1,0,-1};

void p(const vector<vector<char> >& v){
  for( int i = 0;i< v.size();i++){
    for( int j=0;j<v[i].size();j++){
      cout<<v[i][j];
    }
    cout<<endl;
  }
}

void pm(const map<char,pair<pair<int,int>,pair<int,int> > > m ){
  for(map<char,pair<pair<int,int>,pair<int,int> > >::const_iterator it = m.begin();
      it!=m.end();
      it++){

    cout<<it->first<<","<<it->second.first.first<<","<<it->second.first.second<<","<<it->second.second.first<<","<<it->second.second.second<<endl;
  }
}

bool ok(const vector<vector<char> >& v){
  for(int i = 0;i<v.size();i++){
    for( int j = 0;j<v[i].size();j++){
      if(v[i][j] == '?' )return false;
    }
  }
  return true;
}

bool fil(vector<vector<char> >& v,char c, int y, int x, int mr,int mc ){
  bool res = false;
  //  cout<<"fill ("<<y<<","<<x<<") to ("<<mr<<","<<mc<<") to "<<c<<endl;
  for(int i = min(y,mr);i<=max(y,mr);i++){
    for( int j = min(x,mc);j<=max(x,mc);j++){
      if( v[i][j]=='?'){
        res = true;
        v[i][j]=c;
      }else if( v[i][j]!=c){
        return false;
      }
    }
  }
  return res;
  
}
vector<vector<char> > f(const map<char,pair<pair<int,int>,pair<int,int> > >& m,const vector<vector<char> >& v){
  if( ok(v))return v;

  
  set<char> s;
  for(int i = 0;i<R;i++){
    for(int j = 0;j<C;j++){
      if(v[i][j]!= '?' && !s.count(v[i][j]) ){
        s.insert(v[i][j]);
        for( int k = 0;k<R;k++){
          for( int l = 0;l<C;l++){
            vector<vector<char> > lv = v;
            map<char,pair<pair<int,int>,pair<int,int> > > lm = m;
            lm[lv[i][j]].first.first   = min( lm[lv[i][j]].first.first, k );
            lm[lv[i][j]].first.second  = max( lm[lv[i][j]].first.second, k);
            lm[lv[i][j]].second.first  = min(lm[lv[i][j]].second.first,l);
            lm[lv[i][j]].second.second = max(lm[lv[i][j]].second.second,l);
            if(m==lm)continue;
            //            cout<<"v="<<endl;
            //            pm(lm);
            //            cout<<lv[i][j]<<endl;
            //            p(lv);
            if(!fil(lv,
                    lv[i][j],
                    lm[lv[i][j]].first.first,
                    lm[lv[i][j]].second.first,
                    lm[lv[i][j]].first.second,
                    lm[lv[i][j]].second.second))continue;

            //            cout<<"lv="<<endl;
            //            p(lv);

            vector<vector<char> > rv = f(lm,lv);
            if( !rv.empty() )return rv;
          }
        }
      }
    }
  }
  return vector<vector<char> >();
}

void cn(map<char,pair<pair<int,int>,pair<int,int> > >& m,vector<vector<char> >& v ){
  for(map<char,pair<pair<int,int>,pair<int,int> > >::iterator it = m.begin();it!=m.end();it++){
    fil(v,
        it->first,
        it->second.first.first,
        it->second.second.first,
        it->second.first.second,
        it->second.second.second);
  }
}
      

int main(void){
  int T;
  cin>>T;
  for( int c=1;c<=T;c++){
    cin>>R>>C;
    cout<<"Case #"<<c<<":"<<endl;
    vector<vector<char> > cake;
    map<char,pair<pair<int,int>,pair<int,int> > > m;
    for(int i = 0;i<R;i++){
      cake.push_back(vector<char>());
      cake[i].resize(C);
    }
    for(int i = 0;i<R;i++){
      for(int j = 0;j<C;j++){
        cin>>cake[i][j];
        if( cake[i][j]=='?' ) continue;
        if(m.count(cake[i][j])){
            m[cake[i][j]].first.first=min(m[cake[i][j]].first.first,i);
            m[cake[i][j]].first.second=max(m[cake[i][j]].first.second,i);
            m[cake[i][j]].second.first=min(m[cake[i][j]].second.first,j);
            m[cake[i][j]].second.second=min(m[cake[i][j]].second.second,j);
          }else{
            m[cake[i][j]].first.first   = i;
            m[cake[i][j]].first.second  = i;
            m[cake[i][j]].second.first  = j;
            m[cake[i][j]].second.second = j;
          }
      }
    }
    //    cout<<"cake="<<endl;
    //    p(cake);
    //    pm(m);
    //    cn(m,cake);
    //    cout<<"cake="<<endl;
    //    p(cake);
    cake = f(m,cake);
    for(int i = 0;i<R;i++){
      for(int j = 0;j<C;j++){
        cout<<cake[i][j];
      }
      cout<<endl;
    }
  }
  return 0;
}
