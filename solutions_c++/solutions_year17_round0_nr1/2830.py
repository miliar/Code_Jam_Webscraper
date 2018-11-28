#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <climits>
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define mp make_pair
using namespace std;

/**
 * Check for current state to be in the final state
 */
bool isSmiley(string s){
  FOR(i,0,s.length()){
    if (s[i] != '+'){
      return false;
    }
  }
  return true;
}

long int get_min_flip(string s,int k){
  //cout<<"str = "<<s<<endl;
  long int result = 0;
  FOR(i,0,s.length()-k+1){
    if(s[i]=='-'){
      result ++;
      FOR(j,i,i+k){
	if(s[j] == '+'){
	  s[j] = '-';
	}else{
	  s[j] = '+';
	}
      }
    }
  }
  if(!isSmiley(s)){
    //cout<<s<<endl;
    return -1;
  }else{
    return result;
  }
}

int main(){
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int tt;
  cin>>tt;
  FOR(ttnum,1,tt+1){
    string s;
    int k;
    cin>>s;
    cin>>k;
    bool isPoss = true;
    long int min_flip = get_min_flip(s,k);
    if(min_flip == -1){
      isPoss = false;
    }
    /*map<string,bool> al_processed;
    queue<pair<string,int> > q;
    int k;
    string s;
    cin>>s;
    cin>>k;
    q.push(mp(s,0));
    int count = 0;
    int max_found = INT_MAX;
    bool isPoss = false;
    al_processed[s] = true;
    while(!q.empty()){
      string curr_s = q.front().first;
      count = q.front().second;
      if (isSmiley(curr_s)){
	isPoss = true;
	if(count < max_found){
	  max_found = count;
	}
      }
      q.pop();
      string new_str = curr_s;
      FOR(i,0,curr_s.length()-k+1){
	if (curr_s[i] == '-'){
	  new_str = curr_s;
	  FOR(j,i,i+k){
	    if(new_str[j] == '+'){
	      new_str[j] = '-';
	    }else{
	      new_str[j] = '+';
	    }
	  }
	}
	if(al_processed.find(new_str)==al_processed.end()){
	  al_processed[new_str] = true;
	  q.push(mp(new_str,count+1));
	}
      }
      }*/
    cout<<"Case #"<<ttnum<<": ";
    if(isPoss){
      cout<<min_flip<<endl;
    }else{
      cout<<"IMPOSSIBLE"<<endl;
    }
  }
  return 0;
}
