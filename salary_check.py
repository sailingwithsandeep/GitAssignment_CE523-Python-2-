class Per_Emp:
    base_salary = 5000
    def check_salary(self,exp):
        if(exp>=15):
            self.base_salary+=(self.base_salary*20)/100
        elif(exp>=10 and exp<15):
            self.base_salary+=(self.base_salary*10)/100
        elif(exp>=5 and exp<10):
            self.base_salary+=(self.base_salary*5)/100
        return self.base_salary