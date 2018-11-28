#include <iostream>
#include <string>
#include <math.h>
#include <queue>

using namespace std;

struct Node{
	unsigned long long start;
	unsigned long long end;
	unsigned long long index;
	
	bool operator<(const Node& b) const{
	  if((this->end-this->start) == (b.end-b.start)){
			return this->index > b.index;
	  }
	  return (this->end-this->start) < (b.end-b.start);
	}
	
	Node(unsigned long long start,unsigned long long end){
		this->start=start;
		this->end=end;
		this->index=floor((end-start)/2)+start;
	}
};

int main() {
  int t;
  unsigned long long N,K;

  cin >> t;
  for (int i = 1; i <= t; ++i) {
  	std::priority_queue<Node> pq;
    cin >> N >> K;
    pq.push(Node(0,N-1));
	for(int k=1;k<K;k++){
		Node node = pq.top();
		pq.pop();
		//cout<<"Dividing:"<<node.start<<"->"<<node.end<<"("<<node.index<<")"<<endl;
		if(node.end-node.start>1){
			unsigned long long middle=floor((node.end-node.start)/2)+node.start;
			pq.push(Node(node.start,middle-1));
			//cout<<"Added "<<(node.start)<<"=>"<<(middle-1)<<endl;
			pq.push(Node(middle+1,node.end));
			//cout<<"Added "<<(middle+1)<<"=>"<<(node.end)<<endl;
		}
		else if(node.end-node.start==1){
			pq.push(Node(node.start,node.start));
			pq.push(Node(node.end,node.end));
		}
	}
	Node node = pq.top();
	pq.pop();
	//cout<<"Chosing:"<<node.start<<"->"<<node.end<<"("<<node.index<<")"<<endl;
	unsigned long long L = node.index-node.start;
	unsigned long long R = node.end-node.index;
	cout << "Case #" << i << ": "<<max(L,R)<<' '<<min(L,R)<<endl;
  }

  return 0;
}