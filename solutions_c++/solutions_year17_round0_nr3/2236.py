#include <iostream>
#include <fstream>

using namespace std;
void calc_tuple(long long N, long long K, long long (&result)[2]);
bool is_even(long long val);


int main(){

  int num_cases;
  long long N;
  long long K;
  long long result[2]= {0};

  ifstream infile("C-large.in", ifstream::binary);
  ofstream outfile ("output3.txt",ofstream::binary);
  infile>>num_cases;

  for(int i=0;i<num_cases;i++){
    infile>>N;
    infile>>K;
    calc_tuple(N,K, result);
    outfile<<"Case #"<<i+1<<": "<<result[0]<<" "<<result[1]<<endl;
  }

  infile.close();
  outfile.close();
  return 0;
}


void calc_tuple(long long N, long long K, long long (&result)[2]){

  // there will be at least 1 person.
  long long totalcount=1;
  long long nextcount = 2;

  long long thisevenvalue;
  long long thisoddvalue;
  long long thisevencount;
  long long thisoddcount;
  // the status when the first person goes in
  long long tmp = N/2;

  if (is_even(tmp)){
    thisevenvalue = tmp;
    thisoddvalue = tmp-1;

    thisevencount = N%2==1 ? 2 : 1;
    thisoddcount = N%2==1 ? 0 : 1;
  } else {
    thisevenvalue = tmp-1;
    thisoddvalue = tmp;

    thisevencount = N%2==1 ? 0 : 1;
    thisoddcount = N%2==1 ? 2 : 1;
  }

  if(K==1){
    if(thisoddcount ==2){
      result[0] = thisoddvalue;
      result[1] = thisoddvalue;

    } else if(thisevencount ==2){
      result[0] = thisevenvalue;
      result[1] = thisevenvalue;

    } else{
      result[0] = thisevenvalue > thisoddvalue ? thisevenvalue : thisoddvalue;
      result[1] = thisevenvalue > thisoddvalue ? thisoddvalue : thisevenvalue;
    }
    return;
  }
  // values for the next round
  long long nextevenvalue;
  long long nextoddvalue;
  long long nextevencount=0;
  long long nextoddcount=0;

  while(totalcount+nextcount< K){
    tmp = thisevenvalue/2;
    // if 1/2 of the even is still even
    if(is_even(tmp)){
      nextevenvalue = tmp;
      nextoddvalue = tmp-1;

      // if oddvalue is larger, 1/2 of odd value
      if(thisoddvalue>thisevenvalue){
        nextevencount = thisevencount+2*thisoddcount;
        nextoddcount  = thisevencount;
      } else {
        nextevencount = thisevencount;
        nextoddcount = thisevencount+ 2*thisoddcount;
      }

    } else {
      nextevenvalue = tmp-1;
      nextoddvalue = tmp;

      if(thisoddvalue>thisevenvalue){
        nextoddcount = thisevencount+2*thisoddcount;
        nextevencount  = thisevencount;
      } else {
        nextoddcount = thisevencount;
        nextevencount = thisevencount+ 2*thisoddcount;
      }
    }

    thisevenvalue = nextevenvalue;
    thisoddvalue = nextoddvalue;
    thisevencount = nextevencount;
    thisoddcount = nextoddcount;

    totalcount+=nextcount;
    nextcount = nextcount*2;
  }


  if (thisoddvalue>thisevenvalue){
    if(K-totalcount<=thisoddcount){
      //cout<<thisoddvalue/2<<" "<<thisoddvalue/2<<endl;
      result[0] = thisoddvalue/2;
      result[1] = thisoddvalue/2;
    } else {
      //cout<<thisevenvalue/2-1<<" "<<thisevenvalue/2<<endl;
      result[0] = thisevenvalue/2;
      result[1] = thisevenvalue/2-1;
    }

  } else {
    if(K-totalcount<=thisevencount){
      //cout<<thisevenvalue/2-1<<" "<<thisevenvalue/2<<endl;
      result[0] = thisevenvalue/2;
      result[1] = thisevenvalue/2-1;
    } else {
      //cout<<thisoddvalue/2<<" "<<thisoddvalue/2<<endl;
      result[0] = thisoddvalue/2;
      result[1] = thisoddvalue/2;
    }
  }


}

bool is_even(long long val){

  return (val%2==0);

}
