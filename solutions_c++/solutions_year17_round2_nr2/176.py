#include <iostream>
#include <string>

using namespace std;


char letter[3][2];

int counts[3][2];

void init() {
  letter[0][0]='R';
  letter[1][0]='B';
  letter[2][0]='Y';
  letter[0][1]='G';
  letter[1][1]='O';
  letter[2][1]='V';
}

/*pair<int,int> from_let(char c) {
  for(int i=0; i<3; i++) {
    for(int j=0; j<2; j++) {
      if (c==letter[i][j])
	return make_pair(i,j);
    }
  }
  cerr << "Err" << endl;
  return make_pair(0,0);
  }*/





int main() {

  init();
  
  int T;

  cin >> T;


  for(int t=1; t<=T; t++) {
    int N;

    cin >> N;

    cin >> counts[0][0] >> counts[1][1] >> counts[2][0] >> counts[0][1] >> counts[1][0] >> counts[2][1];

    int a=counts[0][0]-counts[0][1];
    int b=counts[1][0]-counts[1][1];
    int c=counts[2][0]-counts[2][1];
    int x=b+c-a;
    int y=a+c-b;
    int z=a+b-c;
    int edges[3]={x,y,z};
    cout << "Case #" << t << ": ";
    if (a<0 || b<0 || c<0 || x<0 || y<0 || z<0 ||
	(a==0 && counts[0][0]!=0 && N!=2*counts[0][0]) ||
	(b==0 && counts[1][0]!=0 && N!=2*counts[1][0]) ||
	(c==0 && counts[2][0]!=0 && N!=2*counts[2][0])) {
      cout << "IMPOSSIBLE" << endl;
    }
    else {
      int l=0;
      int now;
      if (counts[0][0]!=0)
	now=0;
      else if (counts[1][0]!=0)
	now=1;
      else if (counts[2][0]!=0)
	now=2;
      else
	cerr << "HUH??" << endl;
      int start=now;
      //cout << letter[now][0];
      //counts[now][0]--;
      bool finished=false;
      //      cout << "Possible" << endl;
      int last=1;
      bool initial=true;
      while (!finished) {
	//cout << "Looping" << endl;
	while (counts[now][1]>0) {
	  cout << letter[now][1];
	  cout << letter[now][0];
	  counts[now][1]--;
	  counts[now][0]--;
	  l+=2;
	}
	if (edges[(now+last)%3]>0) {
	  edges[(now+last)%3]--;
	  now=(now+2*last)%3;
	  cout << letter[now][0];
	  l++;
	} else if (edges[(now+2*last)%3]>0) {
	  edges[(now+2*last)%3]--;
	  now=(now+last)%3;
	  cout << letter[now][0];
	  last*=2;
	  l++;
	} else {
	  finished=true;
	}
	if (!initial)
	  last*=2;
	initial=false;
	last = (last%3);
      }
      if (now!=start)
	cerr << "MISMATCH" << endl;
      if (l!=N)
	cerr << "missed some" << endl;
      
      cout << endl;
    }
  }
  return 0;
}




      
      
	
    
