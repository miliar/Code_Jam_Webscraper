#include <iostream>
#include <queue>
#include <unordered_map>

void push_down(std::vector<std::pair<long long, long long> >& heap,std::unordered_map<long long, long long>& handle){
	long long curr=0;
	while(curr<heap.size()){
		if(curr*2+1<heap.size()&&heap[curr].first<heap[curr*2+1].first){
			std::pair<long long, long long> temp=heap[curr];
			heap[curr]=heap[curr*2+1];
			heap[curr*2+1]=temp;
			handle[heap[curr].first]=curr;
			handle[heap[curr*2+1].first]=curr*2+1;
			curr=curr*2+1;
		}else if(curr*2+2<heap.size()&&heap[curr].first<heap[curr*2+2].first){
			std::pair<long long,long long> temp=heap[curr];
			heap[curr]=heap[curr*2+2];
			heap[curr*2+2]=temp;
			handle[heap[curr].first]=curr;
			handle[heap[curr*2+2].first]=curr*2+2;
			curr=curr*2+2;
		}else{
			curr=heap.size();
		}
	}
}

void push_up(std::vector<std::pair<long long, long long> >& heap,std::unordered_map<long long, long long>& handle){
	long long curr=heap.size()-1;
	while(curr>0){
		if(heap[curr].first>heap[curr/2].first){
			std::pair<long long, long long> temp=heap[curr];
			heap[curr]=heap[curr/2];
			heap[curr/2]=temp;
			handle[heap[curr].first]=curr;
			handle[heap[curr/2].first]=curr/2;
			curr/=2;
		}else{
			curr=0;
		}
	}
}

int main(){
	int test;
	std::cin>>test;

	for(int t=1;t<=test;++t){

		std::vector<std::pair<long long, long long> > heap;
		std::unordered_map<long long, long long> handle;

		long long size,people;
		std::cin>>size>>people;

		heap.push_back(std::make_pair(size,1));
		handle[size]=0;
		long long left=0;
		long long right=0;

		while(people>0){
			long long avail=heap[0].second;
			long long select=heap[0].first;
			left=(select/2)-1+select%2;
			right=(select/2);
			if(people>avail){
				people-=avail;
				heap[0]=heap[heap.size()-1];
				handle[heap[0].first]=0;
				heap.pop_back();
				handle.erase(select);
				--select;
				push_down(heap,handle);
				if(select>1){
					if(handle.find(select/2)!=handle.end()){
						heap[handle[select/2]].second+=avail;
					}else{

						handle[select/2]=heap.size();
						heap.push_back(std::make_pair(select/2,avail));
						push_up(heap,handle);
					}
					if(handle.find(select/2 + select%2)!=handle.end()){
						heap[handle[(select/2)+ select%2]].second+=avail;
					}else{
						handle[select/2 + select%2]=heap.size();
						heap.push_back(std::make_pair(select/2 + select%2,avail));
						push_up(heap,handle);
					}
				}else{
					if(select==1){
						if(handle.find(1)!=handle.end()){
							heap[handle[1]].second+=avail;
						}else{
							handle[1]=heap.size();
							heap.push_back(std::make_pair(1,avail));
							push_up(heap,handle);
						}
					}
				}


			}else{
				people=0;
				left=(select/2)-1+select%2;
				right=(select/2);
			}


		}
		std::cout<<"Case #"<<t<<": "<<std::max(left,right)<<' '<<std::min(left,right)<<'\n';
	}

	return 0;

}
