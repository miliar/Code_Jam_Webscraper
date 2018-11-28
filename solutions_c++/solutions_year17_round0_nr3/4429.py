#include <cstring>
#include <iostream>
#include <queue>
using namespace std;

struct   miObjecto {
  int initialPos;
  int lenght;

  bool operator<(const miObjecto& lhs) const
  {
    return (lhs.lenght > lenght or (lhs.lenght == lenght and lhs.initialPos < initialPos));
  }
};

int main() {
  int nex;
  int totalPeople;
  int totalBath;
  priority_queue<miObjecto> myp;
  miObjecto el;
  miObjecto elLeft;
  miObjecto elRight;
  
  cin >> nex;

  for(int indEx = 1; indEx <= nex; indEx++) {
    cin >> totalBath;
    cin >> totalPeople;

    myp = priority_queue<miObjecto> ();
    el.initialPos = 1;
    el.lenght = totalBath;
    myp.push(el);		
    
    
    for(int i=0; i < (totalPeople-1); i++) {
      el = myp.top();
      myp.pop();
      if(el.lenght > 2) {
	elLeft.initialPos = el.initialPos;
	elLeft.lenght = (el.lenght-1)/2;
	elRight.initialPos = el.initialPos+(el.lenght-1)/2+1;
	elRight.lenght = (el.lenght)/2;
	myp.push(elLeft);	
	myp.push(elRight);	
      } else if (el.lenght == 2) {
	elRight.initialPos = el.initialPos+1;
	elRight.lenght = 1;
	myp.push(elRight);		
      }
    }

    el = myp.top();
    cout << "Case #" << indEx << ": " << (el.lenght)/2 << " " << (el.lenght-1)/2  << endl;
  }   
}
