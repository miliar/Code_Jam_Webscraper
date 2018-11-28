#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
#define mp make_pair
#define FOR(i,a,b) for(int i=a;i<=b;i++)
using namespace std;
typedef unsigned long int uli;
pair<uli,uli> position;
bool pos_found;

pair<uli,uli> get_val(uli L,uli R){
  pair<uli,uli> ret_val = mp(0,0);
  uli waynum = (R-L);
  if(L>R){
    waynum=0;
  }
  ret_val.first = waynum/2;
  ret_val.second = waynum - ret_val.first;
  return ret_val;
}

pair<uli,uli> get_choice(uli L, uli R, uli K){
  if(pos_found){
    return position;
  }
  
  if(K==1){
    pos_found  = true;
    //cout<<"val="<<L<<" - "<<R<<" - "<<K<<endl;
    return position = get_val(L,R);
  }else{
    uli range = R-L;
    uli mid;
    pair<uli,uli> ret_val;
    mid = range/2;
    mid = L+mid;
    /*if((range%2)==0){
      mid = L+(range/2)-1;
      }else{
      mid = L + (range/2);
      }*/
    //cout<<"val="<<L<<" - "<<mid<<" - "<<R<<" - "<<K<<endl;
    if((K%2)==0){
      ret_val  = get_choice(mid+1,R,K/2);
    }else{
      ret_val = get_choice(L,mid-1,K/2);
    }
    //if((R-mid)>(mid-L)){
    //ret_val = get_choice(mid+1,R,K/2);
      /*if((K%2)==0){
	ret_val = get_choice(mid+1,R,K/2);
      }else{
	ret_val = get_choice(mid+1,R,K/2+1);
	}*/
    //}else{
    //ret_val = get_choice(L,mid-1,K/2);
      /*if((K%2)==0){
	ret_val = get_choice(L,mid-1,K/2);
      }else{
	ret_val = get_choice(L,mid-1,K/2+1);
	}*/
    //}
    return ret_val;
  }
}

int main(){
  //freopen("input.txt","r",stdin);
  //freopen("output.txt","w",stdout);
  
  int tt;
  cin>>tt;
  FOR(ttnum,1,tt){
    uli n,k;
    cin>>n>>k;
    bool found[n];
    //FOR(i,0,n-1){
    //found[i] = false;
    //}
    int LS=0,RS=0;
    int placing_index = -1;
    /*    FOR(kk,1,k){
      LS = -1;
      int first_false_index = -1;
      int last_false_index = -1;
      FOR(i,0,n-1){
	if(!found[i]){
	  if(i>0){
	    for(int j=i-1;j>=0;j--){
	      if(found[j]){
		first_false_index = j+1;
		break;
	      }
	      if(j==0){
		first_false_index = 0;
	      }
	    }
	  }else{
	    first_false_index = 0;
	  }
	  if((i+1)<n){
	    FOR(j,i+1,n-1){
	      if(found[j]){
		last_false_index = j - 1;
		break;
	      }
	      if(j==(n-1)){
		last_false_index = j;
	      }
	    }
	  }else{
	    last_false_index = n-1;
	  }
	
	  int left_val = (i - first_false_index);
	  int right_val = (last_false_index - i);
	  //  cout<<first_false_index<<" - "<<last_false_index<<" - "<<" - "<<i<<" - "<<left_val<<" - "<<right_val<<" - "<<LS<<" - "<<RS<<endl;
	
	  //cout<<left_val<<" - "<<right_val<" - "<<endl;
	  //if((min(left_val,right_val)>=LS) && (max(left_val,right_val)>=RS)){
	  if((last_false_index-first_false_index)%2==0){
	    if(min(left_val,right_val)>LS){
	      placing_index = i;
	      LS = min(left_val,right_val);
	      RS = max(left_val,right_val);
	    }
	  }else{
	    if(min(left_val,right_val)>=LS){
	      placing_index = i;
	      LS = min(left_val,right_val);
	      RS = max(left_val,right_val);
	    }
	  }
	}
      }
      //cout<<kk<<" - placing_index ="<<placing_index<<endl;
      if (placing_index !=-1){
	found[placing_index] = true;
      }
      //int key;
      //cin>>key;
      
      //cout<<RS<<" - "<<LS<<" - "<<kk<<endl;
	
      
	

      }*/
    //cout<<LS<<" " <<RS<<endl;
    pos_found = false;
    pair<uli,uli> result;
    result = get_choice(0,n-1,k);
    //cout<<"Case #"<<ttnum<<": "<<RS<<" "<<LS<<endl;
    cout<<"Case #"<<ttnum<<": "<<result.second<<" "<<result.first<<endl;
    
  }
  return 0;
}
      
